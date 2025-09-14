#!/usr/bin/env node

/**
 * Manual Static HTML Generator for Professor Peptides
 * Creates individual HTML files by serving and capturing each route
 */

const fs = require('fs');
const path = require('path');
const { execSync, spawn } = require('child_process');
const { parse } = require('node-html-parser');

const BUILD_DIR = path.join(__dirname, '../build');
const PORT = 5555; // Use different port to avoid conflicts

// Load routes
const routesFile = path.join(__dirname, 'staticRoutes.js');
const allRoutes = require(routesFile);

console.log('🚀 Manual Static HTML Generation Starting...');
console.log(`📄 Generating ${allRoutes.length} static HTML files\n`);

/**
 * Start a simple HTTP server for the build directory
 */
function startServer() {
  return new Promise((resolve, reject) => {
    const server = spawn('npx', ['serve', '-s', 'build', '-l', PORT.toString()], {
      cwd: path.join(__dirname, '..'),
      stdio: ['ignore', 'pipe', 'pipe']
    });

    let resolved = false;

    server.stdout.on('data', (data) => {
      const output = data.toString();
      if (output.includes('Serving') || output.includes('Local:')) {
        if (!resolved) {
          resolved = true;
          console.log('✅ Server started successfully');
          setTimeout(() => resolve(server), 2000); // Wait 2s for full startup
        }
      }
    });

    server.stderr.on('data', (data) => {
      console.error('Server error:', data.toString());
    });

    server.on('error', (error) => {
      if (!resolved) {
        resolved = true;
        reject(error);
      }
    });

    // Timeout after 10 seconds
    setTimeout(() => {
      if (!resolved) {
        resolved = true;
        reject(new Error('Server startup timeout'));
      }
    }, 10000);
  });
}

/**
 * Fetch HTML content for a route
 */
async function fetchRouteHTML(route) {
  try {
    const url = `http://localhost:${PORT}${route}`;
    
    // Use curl to fetch the content
    const command = `curl -s --max-time 10 "${url}"`;
    const html = execSync(command, { encoding: 'utf8', timeout: 15000 });
    
    if (!html || html.length < 100) {
      throw new Error('Empty or invalid HTML response');
    }
    
    return html;
  } catch (error) {
    console.error(`❌ Failed to fetch ${route}:`, error.message);
    return null;
  }
}

/**
 * Process HTML content for static use
 */
function processHTMLForStatic(html, route) {
  const root = parse(html);
  
  // Remove service worker registration scripts
  const scripts = root.querySelectorAll('script');
  scripts.forEach(script => {
    const content = script.innerHTML;
    if (content.includes('serviceWorker') || content.includes('sw-advanced')) {
      script.remove();
    }
  });
  
  // Ensure all asset links are relative
  const links = root.querySelectorAll('link[href]');
  links.forEach(link => {
    const href = link.getAttribute('href');
    if (href && href.startsWith('/') && !href.startsWith('//')) {
      link.setAttribute('href', '.' + href);
    }
  });
  
  const scriptTags = root.querySelectorAll('script[src]');
  scriptTags.forEach(script => {
    const src = script.getAttribute('src');
    if (src && src.startsWith('/') && !src.startsWith('//')) {
      script.setAttribute('src', '.' + src);
    }
  });
  
  return root.toString();
}

/**
 * Save HTML file for a route
 */
function saveRouteHTML(route, html) {
  const fileName = route === '/' ? 'index.html' : 
    route.replace(/^\//, '').replace(/\//g, '-') + '.html';
  
  const filePath = path.join(BUILD_DIR, fileName);
  
  try {
    fs.writeFileSync(filePath, html, 'utf8');
    console.log(`  ✅ ${fileName}`);
    return true;
  } catch (error) {
    console.error(`❌ Failed to save ${fileName}:`, error.message);
    return false;
  }
}

/**
 * Generate all static HTML files
 */
async function generateAllFiles(server) {
  console.log('📝 Generating static HTML files...\n');
  
  let successful = 0;
  let failed = 0;
  
  // Process routes in batches to avoid overwhelming the server
  const batchSize = 5;
  
  for (let i = 0; i < allRoutes.length; i += batchSize) {
    const batch = allRoutes.slice(i, i + batchSize);
    
    console.log(`📦 Processing batch ${Math.floor(i/batchSize) + 1}/${Math.ceil(allRoutes.length/batchSize)} (${batch.length} routes):`);
    
    const batchPromises = batch.map(async (route) => {
      const html = await fetchRouteHTML(route);
      
      if (html) {
        const processedHTML = processHTMLForStatic(html, route);
        const saved = saveRouteHTML(route, processedHTML);
        
        if (saved) {
          successful++;
        } else {
          failed++;
        }
      } else {
        failed++;
      }
    });
    
    await Promise.all(batchPromises);
    
    // Brief pause between batches
    await new Promise(resolve => setTimeout(resolve, 1000));
  }
  
  console.log(`\n📊 Generation Complete:`);
  console.log(`   ✅ Successful: ${successful} files`);
  console.log(`   ❌ Failed: ${failed} files`);
  
  return { successful, failed };
}

/**
 * Create sitemap for generated files
 */
function createStaticSitemap(successfulRoutes) {
  const sitemap = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${successfulRoutes.map(route => `  <url>
    <loc>https://www.professorpeptides.org${route}</loc>
    <lastmod>${new Date().toISOString().split('T')[0]}</lastmod>
    <priority>${route === '/' ? '1.0' : route.startsWith('/peptide/') ? '0.9' : '0.8'}</priority>
  </url>`).join('\n')}
</urlset>`;

  fs.writeFileSync(path.join(BUILD_DIR, 'sitemap.xml'), sitemap);
  console.log('✅ Static sitemap generated');
}

/**
 * Main execution
 */
async function main() {
  let server;
  
  try {
    // Start server
    console.log('🌐 Starting local server...');
    server = await startServer();
    
    // Wait a bit more for server to be fully ready
    await new Promise(resolve => setTimeout(resolve, 3000));
    
    // Generate all files
    const result = await generateAllFiles(server);
    
    // Create sitemap
    createStaticSitemap(allRoutes.slice(0, result.successful));
    
    console.log(`\n🎉 Manual static generation completed!`);
    console.log(`📁 Files available in: ${BUILD_DIR}`);
    console.log(`🌐 Ready for offline viewing`);
    
  } catch (error) {
    console.error('❌ Generation failed:', error);
    process.exit(1);
  } finally {
    // Clean up server
    if (server) {
      console.log('\n🔚 Shutting down server...');
      server.kill();
    }
  }
}

if (require.main === module) {
  main();
}

module.exports = { main };
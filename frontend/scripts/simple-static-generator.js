#!/usr/bin/env node

/**
 * Simple Static HTML Generator for Professor Peptides
 * Uses existing running server to generate static files
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');
const { parse } = require('node-html-parser');

const BUILD_DIR = path.join(__dirname, '../build');
const SERVER_URL = 'http://localhost:5000'; // Use existing server

// Load routes
const routesFile = path.join(__dirname, 'staticRoutes.js');
const allRoutes = require(routesFile);

console.log('🚀 Simple Static HTML Generation Starting...');
console.log(`📄 Generating ${allRoutes.length} static HTML files\n`);

/**
 * Fetch HTML content for a route
 */
function fetchRouteHTML(route, retries = 2) {
  try {
    const url = `${SERVER_URL}${route}`;
    console.log(`  📥 Fetching: ${route}`);
    
    // Use curl with follow redirects and timeout
    const command = `curl -L -s --max-time 15 "${url}"`;
    const html = execSync(command, { encoding: 'utf8', timeout: 20000 });
    
    if (!html || html.length < 200) {
      throw new Error('Invalid HTML response');
    }
    
    return html;
  } catch (error) {
    if (retries > 0) {
      console.log(`    ⏰ Retrying ${route} (${retries} retries left)...`);
      // Wait 2 seconds before retry
      execSync('sleep 2');
      return fetchRouteHTML(route, retries - 1);
    }
    
    console.error(`    ❌ Failed: ${error.message}`);
    return null;
  }
}

/**
 * Process HTML content for static use
 */
function processHTMLForStatic(html, route) {
  try {
    const root = parse(html);
    
    // Fix asset paths to be relative
    const links = root.querySelectorAll('link[href]');
    links.forEach(link => {
      const href = link.getAttribute('href');
      if (href && href.startsWith('/') && !href.startsWith('//')) {
        // Convert absolute paths to relative
        const depth = (route.match(/\//g) || []).length - 1;
        const prefix = depth > 0 ? '../'.repeat(depth) : './';
        link.setAttribute('href', prefix + href.substring(1));
      }
    });
    
    const scripts = root.querySelectorAll('script[src]');
    scripts.forEach(script => {
      const src = script.getAttribute('src');
      if (src && src.startsWith('/') && !src.startsWith('//')) {
        const depth = (route.match(/\//g) || []).length - 1;
        const prefix = depth > 0 ? '../'.repeat(depth) : './';
        script.setAttribute('src', prefix + src.substring(1));
      }
    });
    
    // Remove problematic service worker scripts for content pages
    const isContentPage = !route.includes('/calculator') && !route.includes('/search') && !route.includes('/quiz');
    
    if (isContentPage) {
      const allScripts = root.querySelectorAll('script');
      allScripts.forEach(script => {
        const content = script.innerHTML;
        const src = script.getAttribute('src');
        
        if (content && (content.includes('serviceWorker') || content.includes('sw-advanced'))) {
          script.remove();
        }
      });
    }
    
    return root.toString();
  } catch (error) {
    console.error(`    ⚠️  HTML processing error: ${error.message}`);
    return html; // Return original if processing fails
  }
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
    console.log(`    ✅ Saved: ${fileName}`);
    return true;
  } catch (error) {
    console.error(`    ❌ Save failed: ${error.message}`);
    return false;
  }
}

/**
 * Test server connectivity
 */
function testServer() {
  try {
    const html = execSync(`curl -s --max-time 5 "${SERVER_URL}/"`, { encoding: 'utf8' });
    if (html && html.includes('Professor Peptides')) {
      console.log('✅ Server is accessible');
      return true;
    } else {
      console.error('❌ Server response invalid');
      return false;
    }
  } catch (error) {
    console.error('❌ Server not accessible:', error.message);
    return false;
  }
}

/**
 * Generate static files for priority routes first
 */
async function generatePriorityFiles() {
  const priorityRoutes = [
    '/',
    '/about',
    '/peptides',
    '/blog',
    '/research',
    '/calculators',
    '/peptide/semaglutide',
    '/peptide/tirzepatide',
    '/peptide/bpc-157'
  ];
  
  console.log('🌟 Generating priority files first...\n');
  
  let successful = 0;
  
  for (const route of priorityRoutes) {
    if (allRoutes.includes(route)) {
      const html = fetchRouteHTML(route);
      
      if (html) {
        const processedHTML = processHTMLForStatic(html, route);
        const saved = saveRouteHTML(route, processedHTML);
        
        if (saved) successful++;
      }
      
      // Brief pause between requests
      execSync('sleep 1');
    }
  }
  
  console.log(`\n✅ Priority files: ${successful}/${priorityRoutes.length}\n`);
  return successful;
}

/**
 * Generate all remaining files
 */
async function generateRemainingFiles(skipRoutes) {
  console.log('📝 Generating remaining files...\n');
  
  const remainingRoutes = allRoutes.filter(route => !skipRoutes.includes(route));
  let successful = 0;
  let failed = 0;
  
  console.log(`📊 Processing ${remainingRoutes.length} remaining routes...\n`);
  
  for (let i = 0; i < remainingRoutes.length; i++) {
    const route = remainingRoutes[i];
    
    if (i % 10 === 0) {
      console.log(`📦 Progress: ${i}/${remainingRoutes.length} completed`);
    }
    
    const html = fetchRouteHTML(route);
    
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
    
    // Brief pause to avoid overwhelming the server
    if (i % 5 === 0) {
      execSync('sleep 1');
    }
  }
  
  console.log(`\n📊 Remaining files complete: ${successful} successful, ${failed} failed`);
  return { successful, failed };
}

/**
 * Main execution
 */
async function main() {
  try {
    // Test server first
    if (!testServer()) {
      throw new Error('Server not accessible. Please ensure the Static Website workflow is running.');
    }
    
    // Wait a moment for server to be ready
    console.log('⏰ Waiting for server to be fully ready...\n');
    execSync('sleep 3');
    
    // Generate priority files first
    const priorityCount = await generatePriorityFiles();
    
    // Generate remaining files
    const priorityRoutes = ['/', '/about', '/peptides', '/blog', '/research', '/calculators', 
                           '/peptide/semaglutide', '/peptide/tirzepatide', '/peptide/bpc-157'];
    
    const result = await generateRemainingFiles(priorityRoutes);
    
    const totalSuccessful = priorityCount + result.successful;
    const totalFailed = result.failed;
    
    console.log(`\n🎉 Static HTML generation completed!`);
    console.log(`📊 Final Results:`);
    console.log(`   ✅ Total successful: ${totalSuccessful} files`);
    console.log(`   ❌ Total failed: ${totalFailed} files`);
    console.log(`   📁 Files location: ${BUILD_DIR}`);
    console.log(`   🌐 Ready for offline viewing with relative paths`);
    
    if (totalSuccessful > 50) {
      console.log(`\n🚀 SUCCESS: Generated ${totalSuccessful} static HTML files!`);
      console.log(`💡 To create ZIP: cd ${BUILD_DIR} && zip -r ../peptide-professor-static.zip .`);
    }
    
  } catch (error) {
    console.error('\n❌ Generation failed:', error.message);
    process.exit(1);
  }
}

if (require.main === module) {
  main();
}

module.exports = { main };
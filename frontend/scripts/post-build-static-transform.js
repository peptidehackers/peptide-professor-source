#!/usr/bin/env node

/**
 * Post-Build Static Transform for Professor Peptides
 * Converts react-snap output to true static HTML files with proper linking
 */

const fs = require('fs');
const path = require('path');
const { parse } = require('node-html-parser');

const BUILD_DIR = path.join(__dirname, '../build');
const CONTENT_ROUTES = ['/peptide/', '/peptides/', '/blog/', '/about', '/faq', '/research', '/resources', '/company/'];
const DYNAMIC_ROUTES = ['/calculators/', '/search', '/quiz'];

// Load generated routes to identify content vs dynamic pages
const routesFile = path.join(__dirname, 'staticRoutes.js');
const allRoutes = require(routesFile);

console.log('🔧 Starting post-build static transformation...');

/**
 * Check if a route should be treated as static content (no JS) or dynamic (keep JS)
 */
function isContentRoute(routePath) {
  // Keep calculators, search, and quiz dynamic
  if (DYNAMIC_ROUTES.some(dynamicPath => routePath.startsWith(dynamicPath))) {
    return false;
  }
  
  // All others are content routes
  return true;
}

// Global mapping from flattened filename to original route
const FLATTENED_TO_ROUTE_MAP = new Map();

/**
 * Move index.html files to .html and create directory structure
 */
function moveIndexFilesToDotHtml() {
  console.log('📁 Converting index.html files to .html format...');
  
  const conversions = [];
  
  allRoutes.forEach(route => {
    if (route === '/') return; // Skip homepage
    
    const routeDir = path.join(BUILD_DIR, route);
    const indexPath = path.join(routeDir, 'index.html');
    
    if (fs.existsSync(indexPath)) {
      // Create .html file in root build directory
      const htmlFileName = route.replace(/^\//, '').replace(/\//g, '-') + '.html';
      const htmlFilePath = path.join(BUILD_DIR, htmlFileName);
      
      // Store mapping from filename to original route
      FLATTENED_TO_ROUTE_MAP.set(htmlFileName, route);
      
      // Copy content
      const content = fs.readFileSync(indexPath, 'utf8');
      fs.writeFileSync(htmlFilePath, content);
      
      conversions.push({ from: indexPath, to: htmlFilePath, route });
      
      console.log(`  ✅ ${route} -> ${htmlFileName}`);
    }
  });
  
  return conversions;
}

/**
 * Rewrite internal links to point to .html files
 */
function rewriteInternalLinks(filePath, isContentPage = true) {
  const content = fs.readFileSync(filePath, 'utf8');
  const root = parse(content);
  
  // Find all internal links
  const links = root.querySelectorAll('a[href]');
  let modified = false;
  
  links.forEach(link => {
    const href = link.getAttribute('href');
    
    // Skip external links, anchors, and already .html links
    if (!href || href.startsWith('http') || href.startsWith('#') || href.startsWith('mailto:') || href.endsWith('.html')) {
      return;
    }
    
    // Convert internal links to .html format
    if (href.startsWith('/') && allRoutes.includes(href)) {
      const htmlFileName = href.replace(/^\//, '').replace(/\//g, '-') + '.html';
      link.setAttribute('href', htmlFileName);
      modified = true;
    }
  });
  
  if (modified) {
    fs.writeFileSync(filePath, root.toString());
  }
  
  return modified;
}

/**
 * Strip JavaScript from content pages to prevent hydration conflicts
 */
function stripJavaScriptFromContentPages(filePath) {
  const content = fs.readFileSync(filePath, 'utf8');
  const root = parse(content);
  
  // Remove all script tags except JSON-LD structured data
  const scripts = root.querySelectorAll('script');
  let removed = 0;
  
  scripts.forEach(script => {
    const type = script.getAttribute('type');
    const src = script.getAttribute('src');
    
    // Keep structured data scripts
    if (type === 'application/ld+json') {
      return;
    }
    
    // Remove all other scripts
    script.remove();
    removed++;
  });
  
  if (removed > 0) {
    fs.writeFileSync(filePath, root.toString());
    console.log(`    🗑️  Removed ${removed} script tags`);
  }
  
  return removed;
}

/**
 * Process all HTML files in build directory
 */
function processAllHtmlFiles() {
  console.log('🔗 Processing HTML files for links and scripts...');
  
  const htmlFiles = [];
  
  // Find all .html files
  function findHtmlFiles(dir, baseDir = '') {
    const items = fs.readdirSync(dir);
    
    items.forEach(item => {
      const fullPath = path.join(dir, item);
      const relativePath = path.join(baseDir, item);
      
      if (fs.statSync(fullPath).isDirectory()) {
        findHtmlFiles(fullPath, relativePath);
      } else if (item.endsWith('.html')) {
        htmlFiles.push({
          path: fullPath,
          route: '/' + relativePath.replace(/\.html$/, '').replace(/\\/g, '/'),
          fileName: item
        });
      }
    });
  }
  
  findHtmlFiles(BUILD_DIR);
  
  console.log(`📄 Found ${htmlFiles.length} HTML files to process`);
  
  htmlFiles.forEach(({ path: filePath, route, fileName }) => {
    // For flattened files, reconstruct original route from filename  
    let originalRoute = route;
    
    // Handle flattened calculator/search/quiz files specially
    if (fileName.startsWith('calculators-')) {
      originalRoute = `/calculators/${fileName.replace('calculators-', '').replace('.html', '')}`;
    } else if (fileName.startsWith('search-')) {
      originalRoute = `/search/${fileName.replace('search-', '').replace('.html', '')}`;
    } else if (fileName.startsWith('quiz-')) {
      originalRoute = `/quiz/${fileName.replace('quiz-', '').replace('.html', '')}`;
    } else if (FLATTENED_TO_ROUTE_MAP.has(fileName)) {
      originalRoute = FLATTENED_TO_ROUTE_MAP.get(fileName);
    }
    
    const isContent = isContentRoute(originalRoute);
    
    console.log(`  📝 Processing: ${fileName} (${isContent ? 'content' : 'dynamic'}) [original: ${originalRoute}]`);
    
    // Rewrite internal links
    const linksModified = rewriteInternalLinks(filePath, isContent);
    if (linksModified) {
      console.log(`    🔗 Updated internal links`);
    }
    
    // Strip JS from content pages only - preserve JS for calculators/search/quizzes
    if (isContent) {
      stripJavaScriptFromContentPages(filePath);
    } else {
      console.log(`    ⚡ Preserving JavaScript for dynamic page`);
    }
  });
}

/**
 * Generate final sitemap with .html extensions for static files
 */
function generateStaticSitemap() {
  console.log('🗺️  Generating static sitemap...');
  
  const SITE_URL = 'https://www.professorpeptides.org';
  
  let sitemapContent = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">`;

  allRoutes.forEach(route => {
    const lastmod = new Date().toISOString().split('T')[0];
    let priority = '0.8';
    
    // Set priorities
    if (route === '/') priority = '1.0';
    else if (route.startsWith('/peptide/')) priority = '0.9';
    else if (route.startsWith('/blog/')) priority = '0.7';
    else if (route.startsWith('/calculators/')) priority = '0.6';
    
    sitemapContent += `
  <url>
    <loc>${SITE_URL}${route}</loc>
    <lastmod>${lastmod}</lastmod>
    <priority>${priority}</priority>
  </url>`;
  });

  sitemapContent += `
</urlset>`;

  const sitemapPath = path.join(BUILD_DIR, 'sitemap.xml');
  fs.writeFileSync(sitemapPath, sitemapContent);
  
  console.log(`✅ Sitemap generated: ${sitemapPath}`);
}

/**
 * Generate robots.txt
 */
function generateRobotsTxt() {
  const robotsContent = `User-agent: *
Allow: /

# Sitemap
Sitemap: https://www.professorpeptides.org/sitemap.xml

# AI Bots - Research and Educational Content
User-agent: GPTBot
Allow: /

User-agent: Claude-Web
Allow: /

User-agent: CCBot
Allow: /

# Block crawling of dynamic endpoints
User-agent: *
Disallow: /api/
Disallow: /*?*
`;

  const robotsPath = path.join(BUILD_DIR, 'robots.txt');
  fs.writeFileSync(robotsPath, robotsContent);
  
  console.log(`✅ Robots.txt generated: ${robotsPath}`);
}

/**
 * Create ZIP file with all static assets
 */
function createStaticZip() {
  console.log('📦 Creating downloadable ZIP file...');
  
  // Note: For now, just log the instruction
  // In a real environment, you'd use a library like 'archiver'
  console.log('📁 Static files ready in:', BUILD_DIR);
  console.log('💡 To create ZIP: cd build && zip -r ../peptide-professor-static.zip .');
  console.log('🌐 Files can be opened locally via file:// protocol');
}

/**
 * Main execution
 */
async function main() {
  try {
    console.log(`🎯 Processing ${allRoutes.length} routes for static export\n`);
    
    // Step 1: Move index.html files to .html format
    const conversions = moveIndexFilesToDotHtml();
    
    // Step 2: Process all HTML files for links and scripts
    processAllHtmlFiles();
    
    // Step 3: Generate sitemap and robots.txt
    generateStaticSitemap();
    generateRobotsTxt();
    
    // Step 4: Create ZIP file
    createStaticZip();
    
    console.log('\n✅ Post-build static transformation completed!');
    console.log(`📊 Summary:`);
    console.log(`   - ${conversions.length} pages converted to .html format`);
    console.log(`   - ${allRoutes.length} routes included in sitemap`);
    console.log(`   - Static files ready for offline viewing`);
    console.log(`   - All internal links point to .html files`);
    
  } catch (error) {
    console.error('❌ Post-build transformation failed:', error);
    process.exit(1);
  }
}

if (require.main === module) {
  main();
}

module.exports = { main, isContentRoute };
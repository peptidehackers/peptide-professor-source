#!/usr/bin/env node
/**
 * Sitemap generation script for Professor Peptides (CommonJS version)
 * Generates sitemap.xml with proper metadata for SEO
 */

const fs = require('fs');
const path = require('path');

// Base configuration
const SITE_URL = 'https://www.professorpeptides.org';
const BUILD_DIR = path.join(__dirname, '../build');

// Define all routes for sitemap generation
const routes = [
  { path: '/', priority: 1.0, changefreq: 'weekly' },
  { path: '/peptides', priority: 0.9, changefreq: 'weekly' },
  { path: '/peptides/browse', priority: 0.8, changefreq: 'weekly' },
  { path: '/research', priority: 0.9, changefreq: 'weekly' },
  { path: '/research/clinical-studies', priority: 0.8, changefreq: 'monthly' },
  { path: '/research/safety-profiles', priority: 0.8, changefreq: 'monthly' },
  { path: '/research/drug-interactions', priority: 0.8, changefreq: 'monthly' },
  { path: '/research/publications', priority: 0.8, changefreq: 'monthly' },
  { path: '/research/updates', priority: 0.8, changefreq: 'weekly' },
  { path: '/research/cognitive', priority: 0.8, changefreq: 'monthly' },
  { path: '/calculators', priority: 0.8, changefreq: 'monthly' },
  { path: '/calculators/bmi', priority: 0.7, changefreq: 'monthly' },
  { path: '/calculators/reconstitution', priority: 0.7, changefreq: 'monthly' },
  { path: '/calculators/protocol', priority: 0.7, changefreq: 'monthly' },
  { path: '/calculators/trt', priority: 0.7, changefreq: 'monthly' },
  { path: '/calculators/melanotan', priority: 0.7, changefreq: 'monthly' },
  { path: '/calculators/glp1', priority: 0.7, changefreq: 'monthly' },
  { path: '/blog', priority: 0.7, changefreq: 'weekly' },
  { path: '/about', priority: 0.6, changefreq: 'monthly' },
  { path: '/faq', priority: 0.6, changefreq: 'monthly' },
  { path: '/company/contact', priority: 0.5, changefreq: 'monthly' },
  { path: '/company/privacy', priority: 0.4, changefreq: 'yearly' },
  { path: '/company/terms', priority: 0.4, changefreq: 'yearly' }
];

// Common peptides for dynamic routes
const peptides = [
  'semaglutide', 'tirzepatide', 'bpc-157', 'tb-500', 'ipamorelin',
  'cjc-1295', 'pt-141', 'melanotan-ii', 'tesamorelin', 'sermorelin',
  'hexarelin', 'ghrp-6', 'ghrp-2', 'thymosin-alpha-1', 'thymosin-beta-4',
  'ghk-cu', 'liraglutide', 'retatrutide', 'epithalon', 'selank', 'semax'
];

// Add peptide detail pages
peptides.forEach(peptide => {
  routes.push({
    path: `/peptide/${peptide}`,
    priority: 0.7,
    changefreq: 'monthly'
  });
});

// Blog categories and articles
const blogCategories = [
  'peptide-basics', 'glp1-agonists', 'growth-hormone-peptides', 
  'healing-peptides', 'cognitive-enhancement', 'anti-aging-peptides',
  'dosing-administration', 'safety-protocols', 'research-methodologies',
  'legal-regulatory', 'performance-peptides', 'immune-system-peptides'
];

// Add blog category pages
blogCategories.forEach(category => {
  routes.push({
    path: `/blog/${category}`,
    priority: 0.6,
    changefreq: 'weekly'
  });
});

// Generate sitemap XML
function generateSitemap() {
  const now = new Date().toISOString().split('T')[0]; // YYYY-MM-DD format
  
  let sitemap = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9
        http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">
`;

  routes.forEach(route => {
    sitemap += `  <url>
    <loc>${SITE_URL}${route.path}</loc>
    <lastmod>${now}</lastmod>
    <changefreq>${route.changefreq}</changefreq>
    <priority>${route.priority}</priority>
  </url>
`;
  });

  sitemap += `</urlset>`;
  
  return sitemap;
}

// Write sitemap to build directory
function writeSitemap() {
  try {
    const sitemapContent = generateSitemap();
    const sitemapPath = path.join(BUILD_DIR, 'sitemap.xml');
    
    // Ensure build directory exists
    if (!fs.existsSync(BUILD_DIR)) {
      fs.mkdirSync(BUILD_DIR, { recursive: true });
    }
    
    fs.writeFileSync(sitemapPath, sitemapContent, 'utf8');
    console.log(`✅ Sitemap generated successfully: ${sitemapPath}`);
    console.log(`📊 Generated ${routes.length} URLs for sitemap`);
    
    return true;
  } catch (error) {
    console.error('❌ Error generating sitemap:', error);
    return false;
  }
}

// Generate robots.txt
function generateRobotsTxt() {
  const robotsContent = `# Professor Peptides - Research Use Only
User-agent: *
Allow: /

# Sitemap
Sitemap: ${SITE_URL}/sitemap.xml

# Crawl-delay for respectful crawling
Crawl-delay: 1

# AI/ML Training - Opt-out
User-agent: GPTBot
Disallow: /

User-agent: Google-Extended
Disallow: /

User-agent: CCBot
Disallow: /

User-agent: anthropic-ai
Allow: /

User-agent: Claude-Web
Allow: /
`;

  try {
    const robotsPath = path.join(BUILD_DIR, 'robots.txt');
    fs.writeFileSync(robotsPath, robotsContent, 'utf8');
    console.log(`✅ Robots.txt generated successfully: ${robotsPath}`);
    return true;
  } catch (error) {
    console.error('❌ Error generating robots.txt:', error);
    return false;
  }
}

// Main execution
if (require.main === module) {
  console.log('🗺️  Generating sitemap and robots.txt for Professor Peptides...');
  const sitemapSuccess = writeSitemap();
  const robotsSuccess = generateRobotsTxt();
  
  const success = sitemapSuccess && robotsSuccess;
  console.log(success ? '✅ All SEO files generated successfully!' : '❌ Some files failed to generate');
  process.exit(success ? 0 : 1);
}

module.exports = { generateSitemap, writeSitemap, generateRobotsTxt };
#!/usr/bin/env node

/**
 * Static Route Generator for Professor Peptides
 * Generates all routes that need to be pre-rendered for static site generation
 */

const fs = require('fs');
const path = require('path');

// Import peptide data to generate dynamic routes
const peptideDataPath = path.join(__dirname, '../src/data/peptideData.js');

// Base static routes
const staticRoutes = [
  '/',
  '/peptides',
  '/peptides/browse', 
  '/research',
  '/resources',
  '/about',
  '/faq',
  '/calculators',
  '/calculators/bmi',
  '/calculators/reconstitution',
  '/calculators/fitness',
  '/calculators/protocol',
  '/calculators/trt',
  '/calculators/melanotan',
  '/blog',
  '/peptides/interactions',
  '/peptides/compatibility',
  '/company/about',
  '/company/contact',
  '/company/careers',
  '/company/press'
];

// Function to extract peptide slugs from peptideData.js
function extractPeptideSlugs() {
  try {
    const peptideDataContent = fs.readFileSync(peptideDataPath, 'utf8');
    
    // Extract all slug values using regex
    const slugMatches = peptideDataContent.match(/"slug":\s*"([^"]+)"/g);
    
    if (!slugMatches) {
      console.log('No peptide slugs found');
      return [];
    }
    
    const slugs = slugMatches.map(match => {
      const slug = match.match(/"slug":\s*"([^"]+)"/)[1];
      return slug;
    });
    
    console.log(`Found ${slugs.length} peptide slugs:`, slugs);
    return slugs;
  } catch (error) {
    console.error('Error reading peptide data:', error);
    return [];
  }
}

// Function to extract blog routes from blog directory
function extractBlogRoutes() {
  const blogRoutes = [];
  const blogDir = path.join(__dirname, '../src/blog');
  
  try {
    const blogCategories = fs.readdirSync(blogDir, { withFileTypes: true })
      .filter(dirent => dirent.isDirectory())
      .map(dirent => dirent.name);
    
    blogCategories.forEach(category => {
      const categoryPath = path.join(blogDir, category);
      const files = fs.readdirSync(categoryPath)
        .filter(file => file.endsWith('.jsx'))
        .map(file => file.replace('.jsx', ''));
      
      files.forEach(file => {
        blogRoutes.push(`/blog/${category}/${file}`);
      });
    });
    
    console.log(`Found ${blogRoutes.length} blog routes`);
    return blogRoutes;
  } catch (error) {
    console.error('Error reading blog routes:', error);
    return [];
  }
}

// Function to extract peptide categories
function extractPeptideCategories() {
  // Known peptide categories from the data structure
  const categories = [
    'metabolicHealth',
    'tissueRepairRecovery', 
    'performanceEnhancement',
    'cognitiveEnhancement',
    'painRelief',
    'skinHealth',
    'immuneSupport'
  ];
  
  console.log(`Found ${categories.length} peptide categories:`, categories);
  return categories;
}

// Function to extract research categories 
function extractResearchCategories() {
  const researchCategories = [
    'clinical-trials',
    'safety-studies', 
    'efficacy-research',
    'mechanism-studies',
    'comparative-analysis',
    'meta-analysis',
    'case-studies',
    'systematic-reviews'
  ];
  
  return researchCategories;
}

// Generate all routes
function generateAllRoutes() {
  const peptideSlugs = extractPeptideSlugs();
  const blogRoutes = extractBlogRoutes();
  const peptideCategories = extractPeptideCategories();
  const researchCategories = extractResearchCategories();
  
  // Generate peptide detail routes
  const peptideDetailRoutes = peptideSlugs.map(slug => `/peptide/${slug}`);
  
  // Generate peptide category routes  
  const peptideCategoryRoutes = peptideCategories.map(category => `/peptides/${category}`);
  
  // Generate research category routes
  const researchCategoryRoutes = researchCategories.map(category => `/research/${category}`);
  
  // Combine all routes
  const allRoutes = [
    ...staticRoutes,
    ...peptideDetailRoutes,
    ...peptideCategoryRoutes,
    ...researchCategoryRoutes,
    ...blogRoutes
  ];
  
  // Remove duplicates and sort
  const uniqueRoutes = [...new Set(allRoutes)].sort();
  
  console.log(`\nGenerated ${uniqueRoutes.length} total routes for static generation:`);
  console.log(`- ${staticRoutes.length} static routes`);
  console.log(`- ${peptideDetailRoutes.length} peptide detail routes`);
  console.log(`- ${peptideCategoryRoutes.length} peptide category routes`); 
  console.log(`- ${researchCategoryRoutes.length} research category routes`);
  console.log(`- ${blogRoutes.length} blog article routes`);
  
  return uniqueRoutes;
}

// Save routes to file for react-snap
function saveRoutes(routes) {
  const routesContent = `// Auto-generated routes for static site generation
// Generated on ${new Date().toISOString()}

module.exports = ${JSON.stringify(routes, null, 2)};
`;

  const outputPath = path.join(__dirname, 'staticRoutes.js');
  fs.writeFileSync(outputPath, routesContent);
  
  console.log(`\nRoutes saved to: ${outputPath}`);
  return outputPath;
}

// Main execution
if (require.main === module) {
  console.log('🚀 Generating static routes for Professor Peptides...\n');
  
  const allRoutes = generateAllRoutes();
  const outputFile = saveRoutes(allRoutes);
  
  console.log('\n✅ Static route generation completed!');
  console.log(`📄 Total routes to pre-render: ${allRoutes.length}`);
  console.log(`💾 Routes file: ${outputFile}`);
}

module.exports = { generateAllRoutes, extractPeptideSlugs, extractBlogRoutes };
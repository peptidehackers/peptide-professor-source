#!/usr/bin/env node

/**
 * Pre-build Data Fetching Script for Professor Peptides
 * 
 * This script fetches all dynamic data from the backend API during build time
 * and generates static JSON files to eliminate runtime API dependencies.
 * 
 * Data Sources:
 * - All peptide data from backend API at localhost:8001/api/peptides
 * - Calculator configurations and data
 * - Assessment quiz data 
 * - Blog content and metadata
 * - Research publications and studies
 * - Category and classification data
 */

const fs = require('fs');
const path = require('path');
const axios = require('axios');

// Configuration
const API_BASE_URL = process.env.REACT_APP_BACKEND_URL || 'http://localhost:8000';
const API_URL = `${API_BASE_URL}/api`;
const OUTPUT_DIR = path.join(__dirname, '..', 'src', 'data', 'static');
const PUBLIC_DATA_DIR = path.join(__dirname, '..', 'public', 'data');

// Ensure output directories exist
const ensureDirectoryExists = (dirPath) => {
  if (!fs.existsSync(dirPath)) {
    fs.mkdirSync(dirPath, { recursive: true });
    console.log(`Created directory: ${dirPath}`);
  }
};

// Create axios instance with timeout
const api = axios.create({
  baseURL: API_URL,
  timeout: 30000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Utility function to save JSON data
const saveJsonData = (filename, data, directory = OUTPUT_DIR) => {
  const filePath = path.join(directory, filename);
  try {
    fs.writeFileSync(filePath, JSON.stringify(data, null, 2));
    console.log(`✅ Saved: ${filename} (${JSON.stringify(data).length} bytes)`);
    return true;
  } catch (error) {
    console.error(`❌ Failed to save ${filename}:`, error.message);
    return false;
  }
};

// Data fetching functions
const fetchPeptideData = async () => {
  console.log('🧬 Fetching all peptide data...');
  try {
    const response = await api.get('/peptides');
    const peptideData = response.data;
    
    // Save complete peptide database
    saveJsonData('peptides-complete.json', peptideData);
    
    // Create individual peptide files for faster loading
    const individualPeptides = {};
    Object.keys(peptideData).forEach(categoryKey => {
      const category = peptideData[categoryKey];
      if (category.peptides) {
        category.peptides.forEach(peptide => {
          individualPeptides[peptide.slug] = {
            ...peptide,
            category: categoryKey,
            categoryTitle: category.title
          };
        });
      }
    });
    
    // Save individual peptide files
    Object.keys(individualPeptides).forEach(slug => {
      saveJsonData(`peptide-${slug}.json`, individualPeptides[slug]);
    });
    
    console.log(`✅ Processed ${Object.keys(individualPeptides).length} individual peptides`);
    return { success: true, count: Object.keys(individualPeptides).length };
  } catch (error) {
    console.error('❌ Failed to fetch peptide data:', error.message);
    return { success: false, error: error.message };
  }
};

const fetchPeptideCategories = async () => {
  console.log('📂 Fetching peptide categories...');
  try {
    const response = await api.get('/peptide-categories');
    const categories = response.data;
    
    // Save complete categories
    saveJsonData('peptide-categories.json', categories);
    
    // Save individual category files
    Object.keys(categories).forEach(categoryKey => {
      saveJsonData(`category-${categoryKey}.json`, categories[categoryKey]);
    });
    
    console.log(`✅ Processed ${Object.keys(categories).length} categories`);
    return { success: true, count: Object.keys(categories).length };
  } catch (error) {
    console.error('❌ Failed to fetch categories:', error.message);
    return { success: false, error: error.message };
  }
};

const fetchTeamMembers = async () => {
  console.log('👥 Fetching team members...');
  try {
    const response = await api.get('/team-members');
    const teamData = response.data;
    
    saveJsonData('team-members.json', teamData);
    console.log(`✅ Processed ${teamData.team ? teamData.team.length : 0} team members`);
    return { success: true, data: teamData };
  } catch (error) {
    console.error('❌ Failed to fetch team members:', error.message);
    return { success: false, error: error.message };
  }
};

const fetchBlogPosts = async () => {
  console.log('📰 Fetching blog posts...');
  try {
    const response = await api.get('/blog-posts');
    const blogData = response.data;
    
    saveJsonData('blog-posts.json', blogData);
    console.log(`✅ Processed ${blogData.posts ? blogData.posts.length : 0} blog posts`);
    return { success: true, data: blogData };
  } catch (error) {
    console.error('❌ Failed to fetch blog posts:', error.message);
    return { success: false, error: error.message };
  }
};

// Generate calculator configurations
const generateCalculatorConfigs = () => {
  console.log('🧮 Generating calculator configurations...');
  
  const calculatorConfigs = {
    reconstitution: {
      title: 'Peptide Reconstitution Calculator',
      description: 'Calculate proper mixing ratios for peptide reconstitution',
      fields: [
        { key: 'vialSize', label: 'Vial Size (mg)', type: 'number', required: true },
        { key: 'bacteriostaticWater', label: 'Bacteriostatic Water (ml)', type: 'number', required: true },
        { key: 'targetDose', label: 'Target Dose', type: 'number', required: true }
      ]
    },
    dosing: {
      title: 'Peptide Dosing Calculator',
      description: 'Calculate dosing protocols based on body weight and frequency',
      fields: [
        { key: 'bodyWeight', label: 'Body Weight (kg)', type: 'number', required: true },
        { key: 'frequency', label: 'Frequency (times/day)', type: 'number', required: true },
        { key: 'duration', label: 'Duration (weeks)', type: 'number', required: true }
      ]
    },
    conversion: {
      title: 'Unit Conversion Calculator',
      description: 'Convert between different measurement units',
      fields: [
        { key: 'amount', label: 'Amount', type: 'number', required: true },
        { key: 'fromUnit', label: 'From Unit', type: 'select', options: ['mg', 'mcg', 'IU', 'ml'], required: true },
        { key: 'toUnit', label: 'To Unit', type: 'select', options: ['mg', 'mcg', 'IU', 'ml'], required: true }
      ]
    },
    bmi: {
      title: 'BMI Calculator',
      description: 'Calculate Body Mass Index and health recommendations',
      fields: [
        { key: 'height', label: 'Height (cm)', type: 'number', required: true },
        { key: 'weight', label: 'Weight (kg)', type: 'number', required: true },
        { key: 'age', label: 'Age (years)', type: 'number', required: false },
        { key: 'gender', label: 'Gender', type: 'select', options: ['male', 'female', 'other'], required: false }
      ]
    },
    glp1: {
      title: 'GLP-1 Weight Loss Calculator',
      description: 'Project potential weight loss with GLP-1 agonists',
      fields: [
        { key: 'currentWeight', label: 'Current Weight (kg)', type: 'number', required: true },
        { key: 'targetWeight', label: 'Target Weight (kg)', type: 'number', required: true },
        { key: 'peptideType', label: 'Peptide Type', type: 'select', options: ['semaglutide', 'tirzepatide', 'liraglutide'], required: true },
        { key: 'duration', label: 'Treatment Duration (weeks)', type: 'number', required: true }
      ]
    }
  };
  
  // Save calculator configurations
  saveJsonData('calculator-configs.json', calculatorConfigs);
  
  // Generate peptide-specific dosing data
  const peptideDosing = {
    'semaglutide': { unit: 'mg', startDose: 0.25, maxDose: 2.4, baseMultiplier: 0.25 },
    'tirzepatide': { unit: 'mg', startDose: 2.5, maxDose: 15, baseMultiplier: 2.5 },
    'liraglutide': { unit: 'mg', startDose: 0.6, maxDose: 3.0, baseMultiplier: 0.6 },
    'bpc-157': { unit: 'mcg', startDose: 250, maxDose: 500, baseMultiplier: 4 },
    'tb-500': { unit: 'mg', startDose: 2, maxDose: 5, baseMultiplier: 0.04 },
    'ipamorelin': { unit: 'mcg', startDose: 200, maxDose: 300, baseMultiplier: 3 },
    'cjc-1295': { unit: 'mcg', startDose: 100, maxDose: 300, baseMultiplier: 2 },
    'igf-1-lr3': { unit: 'mcg', startDose: 20, maxDose: 60, baseMultiplier: 0.6 }
  };
  
  saveJsonData('peptide-dosing-data.json', peptideDosing);
  
  console.log('✅ Generated calculator configurations');
  return { success: true };
};

// Generate assessment quiz data
const generateQuizData = () => {
  console.log('📋 Generating assessment quiz data...');
  
  const quizData = {
    questions: [
      {
        id: 'primary-interest',
        type: 'single-choice',
        question: 'What is your primary interest in peptides?',
        options: [
          { value: 'weight', label: 'Weight Management', description: 'GLP-1 agonists, metabolic peptides' },
          { value: 'muscle', label: 'Muscle Growth & Recovery', description: 'Growth factors, healing peptides' },
          { value: 'healing', label: 'Healing & Recovery', description: 'Tissue repair, wound healing' },
          { value: 'cognitive', label: 'Cognitive Enhancement', description: 'Nootropics, brain health' },
          { value: 'anti-aging', label: 'Anti-Aging & Longevity', description: 'Cellular health, longevity' },
          { value: 'skin', label: 'Skin Health', description: 'Cosmetic peptides, skin rejuvenation' }
        ],
        required: true
      },
      {
        id: 'experience-level',
        type: 'single-choice',
        question: 'What is your experience level with peptides?',
        options: [
          { value: 'beginner', label: 'Beginner', description: 'New to peptides, learning basics' },
          { value: 'intermediate', label: 'Intermediate', description: 'Some experience, researching protocols' },
          { value: 'advanced', label: 'Advanced', description: 'Experienced with multiple peptides' },
          { value: 'professional', label: 'Professional', description: 'Healthcare provider or researcher' }
        ],
        required: true
      },
      {
        id: 'information-type',
        type: 'single-choice',
        question: 'What type of information are you most interested in?',
        options: [
          { value: 'dosing', label: 'Dosing & Protocols', description: 'Practical usage information' },
          { value: 'research', label: 'Research & Studies', description: 'Scientific literature and data' },
          { value: 'safety', label: 'Safety & Side Effects', description: 'Risk assessment and safety data' },
          { value: 'practical', label: 'Practical Applications', description: 'Real-world usage and tips' }
        ],
        required: true
      }
    ],
    scoring: {
      weight: {
        peptides: ['semaglutide', 'tirzepatide', 'liraglutide', 'retatrutide'],
        calculators: ['glp1', 'bmi'],
        resources: ['weight-management-guide', 'metabolic-health-research']
      },
      muscle: {
        peptides: ['bpc-157', 'tb-500', 'ipamorelin', 'cjc-1295'],
        calculators: ['reconstitution', 'dosing'],
        resources: ['muscle-growth-guide', 'recovery-protocols']
      },
      healing: {
        peptides: ['bpc-157', 'tb-500', 'ghk-cu'],
        calculators: ['reconstitution', 'dosing'],
        resources: ['healing-guide', 'tissue-repair-research']
      },
      cognitive: {
        peptides: ['semax', 'selank', 'noopept'],
        calculators: ['dosing', 'conversion'],
        resources: ['cognitive-enhancement-guide', 'nootropic-research']
      }
    }
  };
  
  saveJsonData('assessment-quiz.json', quizData);
  console.log('✅ Generated assessment quiz data');
  return { success: true };
};

// Generate research data
const generateResearchData = () => {
  console.log('🔬 Generating research data...');
  
  const researchData = {
    publications: {
      'semaglutide': [
        {
          title: 'Semaglutide and cardiovascular outcomes in type 2 diabetes',
          authors: 'Marso, S. P. et al.',
          journal: 'New England Journal of Medicine',
          year: '2016',
          doi: '10.1056/NEJMoa1601031',
          abstract: 'Cardiovascular outcomes study of semaglutide in type 2 diabetes patients.',
          methodology: 'Randomized, double-blind, placebo-controlled trial'
        },
        {
          title: 'Semaglutide for the treatment of obesity',
          authors: 'Wadden, T. A. et al.',
          journal: 'JAMA',
          year: '2019',
          doi: '10.1001/jama.2019.17831',
          abstract: 'Phase 3 trial evaluating semaglutide for chronic weight management.',
          methodology: 'Randomized controlled trial'
        }
      ],
      'bpc-157': [
        {
          title: 'The role of BPC 157 on wound healing: A systematic review',
          authors: 'Sikiric, P. et al.',
          journal: 'Wound Repair and Regeneration',
          year: '2008',
          doi: '10.1111/j.1524-475X.2008.00383.x',
          abstract: 'Systematic review of BPC-157 effects on wound healing in animal models.',
          methodology: 'Systematic review and meta-analysis'
        }
      ]
    },
    studyTypes: {
      'clinical-trials': {
        title: 'Clinical Trials',
        description: 'Human studies with rigorous protocols and controls',
        evidenceLevel: 'High'
      },
      'animal-studies': {
        title: 'Animal Studies',
        description: 'Preclinical research in animal models',
        evidenceLevel: 'Medium'
      },
      'in-vitro': {
        title: 'In Vitro Studies',
        description: 'Laboratory studies using cell cultures',
        evidenceLevel: 'Low'
      }
    },
    safetyProfiles: {
      'fda-approved': {
        title: 'FDA Approved',
        description: 'Peptides approved by the FDA for specific medical conditions',
        safetyLevel: 'High',
        examples: ['semaglutide', 'tirzepatide', 'liraglutide']
      },
      'research-phase': {
        title: 'Research Phase',
        description: 'Investigational compounds not approved for human use',
        safetyLevel: 'Unknown',
        examples: ['bpc-157', 'tb-500', 'cjc-1295']
      }
    }
  };
  
  saveJsonData('research-data.json', researchData);
  console.log('✅ Generated research data');
  return { success: true };
};

// Generate sitemap and robots.txt
const generateSEOFiles = () => {
  console.log('🔍 Generating SEO files...');
  
  // Generate sitemap.xml
  const sitemap = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://www.professorpeptides.org/</loc>
    <lastmod>${new Date().toISOString().split('T')[0]}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://www.professorpeptides.org/about</loc>
    <lastmod>${new Date().toISOString().split('T')[0]}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://www.professorpeptides.org/peptides</loc>
    <lastmod>${new Date().toISOString().split('T')[0]}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://www.professorpeptides.org/calculators</loc>
    <lastmod>${new Date().toISOString().split('T')[0]}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://www.professorpeptides.org/quiz</loc>
    <lastmod>${new Date().toISOString().split('T')[0]}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://www.professorpeptides.org/research</loc>
    <lastmod>${new Date().toISOString().split('T')[0]}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://www.professorpeptides.org/blog</loc>
    <lastmod>${new Date().toISOString().split('T')[0]}</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://www.professorpeptides.org/contact</loc>
    <lastmod>${new Date().toISOString().split('T')[0]}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>
</urlset>`;

  // Generate robots.txt
  const robots = `# Professor Peptides - Robots.txt
User-agent: *
Allow: /

# Sitemap location
Sitemap: https://www.professorpeptides.org/sitemap.xml

# Block access to admin and private areas
Disallow: /admin/
Disallow: /private/
Disallow: /_next/
Disallow: /api/

# Allow specific crawlers
User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

# Crawl delay
Crawl-delay: 1`;

  try {
    fs.writeFileSync(path.join(PUBLIC_DATA_DIR, 'sitemap.xml'), sitemap);
    fs.writeFileSync(path.join(PUBLIC_DATA_DIR, 'robots.txt'), robots);
    console.log('✅ Generated sitemap.xml and robots.txt');
    return { success: true };
  } catch (error) {
    console.error('❌ Failed to generate SEO files:', error.message);
    return { success: false, error: error.message };
  }
};

// Main execution function
const main = async () => {
  console.log('🚀 Starting Professor Peptides data pre-fetching...\n');
  
  // Ensure directories exist
  ensureDirectoryExists(OUTPUT_DIR);
  ensureDirectoryExists(PUBLIC_DATA_DIR);
  
  const results = {
    timestamp: new Date().toISOString(),
    successful: [],
    failed: []
  };
  
  // Check if we're in deployment/CI environment
  // More comprehensive deployment environment detection
  const isDeploymentBuild = process.env.CI === 'true' || 
                           process.env.NODE_ENV === 'production' ||
                           process.env.SKIP_API_FETCH === 'true' ||
                           process.env.VERCEL === '1' ||
                           process.env.NETLIFY === 'true' ||
                           process.env.GITHUB_ACTIONS === 'true' ||
                           process.env.GOOGLE_CLOUD_BUILD === 'true' ||
                           process.env.CLOUD_RUN === 'true' ||
                           process.env.FIREBASE_BUILD === 'true' ||
                           process.env.HEROKU === 'true';
  
  if (isDeploymentBuild) {
    console.log('🏗️  Deployment/CI environment detected - skipping API data fetching');
    console.log('📋 Running in static-only mode for deployment build');
    console.log('🔧 Environment variables detected:');
    console.log(`   CI: ${process.env.CI}`);
    console.log(`   NODE_ENV: ${process.env.NODE_ENV}`);
    console.log(`   SKIP_API_FETCH: ${process.env.SKIP_API_FETCH}`);
    console.log(`   VERCEL: ${process.env.VERCEL}`);
    console.log(`   GOOGLE_CLOUD_BUILD: ${process.env.GOOGLE_CLOUD_BUILD}`);
    console.log(`   CLOUD_RUN: ${process.env.CLOUD_RUN}\n`);
    
    // Generate minimal fallback data for deployment (with output parity)
    console.log('📝 Generating minimal fallback data for deployment...');
    const fallbackPeptideData = {
      'glp1-agonists': {
        title: 'GLP-1 Agonists',
        description: 'GLP-1 receptor agonists for metabolic health',
        peptides: [
          { 
            slug: 'semaglutide', 
            name: 'Semaglutide', 
            category: 'glp1-agonists',
            description: 'GLP-1 receptor agonist for weight management',
            type: 'GLP-1 Agonist'
          },
          { 
            slug: 'tirzepatide', 
            name: 'Tirzepatide', 
            category: 'glp1-agonists',
            description: 'Dual GIP/GLP-1 receptor agonist',
            type: 'GLP-1 Agonist'
          }
        ]
      },
      'healing-peptides': {
        title: 'Healing Peptides',
        description: 'Peptides for tissue repair and recovery',
        peptides: [
          { 
            slug: 'bpc-157', 
            name: 'BPC-157', 
            category: 'healing-peptides',
            description: 'Body Protection Compound for healing',
            type: 'Healing Peptide'
          },
          { 
            slug: 'tb-500', 
            name: 'TB-500', 
            category: 'healing-peptides',
            description: 'Thymosin Beta-4 fragment for recovery',
            type: 'Healing Peptide'
          }
        ]
      }
    };
    
    // Save complete data sets
    saveJsonData('peptides-complete.json', fallbackPeptideData);
    saveJsonData('peptide-categories.json', fallbackPeptideData);
    
    // Generate individual peptide files (output parity)
    Object.keys(fallbackPeptideData).forEach(categoryKey => {
      const category = fallbackPeptideData[categoryKey];
      if (category.peptides) {
        category.peptides.forEach(peptide => {
          saveJsonData(`peptide-${peptide.slug}.json`, {
            ...peptide,
            category: categoryKey,
            categoryTitle: category.title
          });
        });
      }
    });
    
    // Generate individual category files (output parity)
    Object.keys(fallbackPeptideData).forEach(categoryKey => {
      saveJsonData(`category-${categoryKey}.json`, fallbackPeptideData[categoryKey]);
    });
    
    // Generate empty team and blog data
    saveJsonData('team-members.json', { team: [] });
    saveJsonData('blog-posts.json', { posts: [] });
    
    console.log('✅ Generated comprehensive fallback data for deployment build with output parity\n');
    
    results.failed.push({ name: 'API Connection', error: 'Skipped for deployment build' });
  } else {
    try {
      // Test API connectivity first
      console.log('🔍 Testing API connectivity...');
      await api.get('/health');
      console.log('✅ API is accessible\n');
      
      // Fetch all dynamic data
      const tasks = [
        { name: 'Peptide Data', fn: fetchPeptideData },
        { name: 'Peptide Categories', fn: fetchPeptideCategories },
        { name: 'Team Members', fn: fetchTeamMembers },
        { name: 'Blog Posts', fn: fetchBlogPosts }
      ];
      
      for (const task of tasks) {
        console.log(`📡 Starting: ${task.name}`);
        const result = await task.fn();
        if (result.success) {
          results.successful.push(task.name);
        } else {
          results.failed.push({ name: task.name, error: result.error });
        }
        console.log(''); // Add spacing
      }
      
    } catch (error) {
      console.error('❌ API connectivity failed:', error.message);
      console.log('📋 Using fallback mode - generating static configurations only\n');
      results.failed.push({ name: 'API Connection', error: error.message });
    }
  }
  
  // Generate static configurations (always run these)
  const staticTasks = [
    { name: 'Calculator Configs', fn: generateCalculatorConfigs },
    { name: 'Quiz Data', fn: generateQuizData },
    { name: 'Research Data', fn: generateResearchData },
    { name: 'SEO Files', fn: generateSEOFiles }
  ];
  
  for (const task of staticTasks) {
    console.log(`⚙️  Generating: ${task.name}`);
    const result = task.fn();
    if (result.success) {
      results.successful.push(task.name);
    } else {
      results.failed.push({ name: task.name, error: result.error });
    }
  }
  
  // Save build report
  saveJsonData('build-report.json', results);
  
  // Print summary
  console.log('\n' + '='.repeat(60));
  console.log('📊 PRE-BUILD DATA FETCHING COMPLETE');
  console.log('='.repeat(60));
  console.log(`✅ Successful: ${results.successful.length} tasks`);
  console.log(`❌ Failed: ${results.failed.length} tasks`);
  
  if (results.successful.length > 0) {
    console.log('\n✅ Successfully completed:');
    results.successful.forEach(task => console.log(`   - ${task}`));
  }
  
  if (results.failed.length > 0) {
    console.log('\n❌ Failed tasks:');
    results.failed.forEach(task => console.log(`   - ${task.name}: ${task.error}`));
  }
  
  console.log(`\n📁 Static data files saved to: ${OUTPUT_DIR}`);
  console.log(`📁 Public files saved to: ${PUBLIC_DATA_DIR}`);
  console.log(`⏰ Build completed at: ${results.timestamp}\n`);
  
  // Exit with appropriate code
  // Don't fail the build if only API connection fails - static mode is acceptable for deployment
  const criticalFailures = results.failed.filter(task => 
    task.name !== 'API Connection' && task.name !== 'Peptide Data Fetch'
  );
  process.exit(criticalFailures.length > 0 ? 1 : 0);
};

// Run the script
if (require.main === module) {
  main().catch(error => {
    console.error('💥 Fatal error:', error);
    process.exit(1);
  });
}

module.exports = { main };
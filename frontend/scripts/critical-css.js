#!/usr/bin/env node

// Critical CSS extraction and inlining script
const critical = require('critical');
const fs = require('fs');
const path = require('path');
const { minify } = require('csso');

const BUILD_DIR = path.join(__dirname, '../build');
const CRITICAL_CSS_FILE = path.join(__dirname, '../src/critical.css');

// Pages to extract critical CSS for
const PAGES = [
  {
    url: '/',
    css: 'critical-home.css',
    dimensions: [
      { width: 320, height: 568 }, // Mobile
      { width: 768, height: 1024 }, // Tablet
      { width: 1200, height: 900 } // Desktop
    ]
  },
  {
    url: '/peptides',
    css: 'critical-peptides.css',
    dimensions: [
      { width: 320, height: 568 },
      { width: 1200, height: 900 }
    ]
  },
  {
    url: '/calculators',
    css: 'critical-calculators.css',
    dimensions: [
      { width: 320, height: 568 },
      { width: 1200, height: 900 }
    ]
  }
];

// Extract critical CSS for above-the-fold content
async function extractCriticalCSS() {
  console.log('🎯 Extracting critical CSS...');
  
  const allCriticalCSS = [];
  
  try {
    for (const page of PAGES) {
      console.log(`📄 Processing ${page.url}...`);
      
      const criticalCSS = await critical.generate({
        base: BUILD_DIR,
        src: `index.html`,
        target: {
          css: page.css,
          html: `${page.url.replace('/', 'home') || 'home'}-critical.html`,
          uncritical: `${page.url.replace('/', 'home') || 'home'}-uncritical.css`
        },
        dimensions: page.dimensions,
        penthouse: {
          timeout: 30000,
          pageLoadSkipTimeout: 10000,
          renderWaitTime: 1000,
          blockJSRequests: false,
          properties: [
            'position',
            'top', 'right', 'bottom', 'left',
            'width', 'height',
            'margin', 'padding',
            'border', 'background',
            'font', 'color',
            'display', 'visibility',
            'z-index', 'opacity'
          ]
        },
        ignore: {
          atrule: ['@font-face'],
          rule: [/\.sr-only/, /\.hidden/],
          decl: (node, value) => {
            // Skip CSS custom properties that aren't critical
            return /^--/.test(node.prop) && !['--tw-bg-opacity', '--tw-text-opacity'].includes(node.prop);
          }
        },
        minify: false // We'll minify separately
      });
      
      allCriticalCSS.push(criticalCSS.css);
      console.log(`✅ Critical CSS extracted for ${page.url} (${criticalCSS.css.length} bytes)`);
    }
    
    // Combine all critical CSS and remove duplicates
    const combinedCSS = deduplicateCSS(allCriticalCSS.join('\n'));
    
    // Minify the combined critical CSS
    const minifiedCSS = minify(combinedCSS).css;
    
    // Write critical CSS to file
    fs.writeFileSync(CRITICAL_CSS_FILE, minifiedCSS, 'utf8');
    console.log(`💾 Combined critical CSS written to ${CRITICAL_CSS_FILE} (${minifiedCSS.length} bytes)`);
    
    // Generate critical CSS stats
    generateCriticalStats(minifiedCSS);
    
    return minifiedCSS;
    
  } catch (error) {
    console.error('❌ Error extracting critical CSS:', error);
    throw error;
  }
}

// Remove duplicate CSS rules
function deduplicateCSS(css) {
  const rules = new Set();
  const lines = css.split('\n').filter(line => {
    const trimmed = line.trim();
    if (!trimmed || rules.has(trimmed)) {
      return false;
    }
    rules.add(trimmed);
    return true;
  });
  
  return lines.join('\n');
}

// Generate stats for critical CSS
function generateCriticalStats(css) {
  const stats = {
    totalSize: css.length,
    rules: (css.match(/}/g) || []).length,
    selectors: (css.match(/[^{}]+(?=\s*{)/g) || []).length,
    mediaQueries: (css.match(/@media[^{]+/g) || []).length,
    fontFaces: (css.match(/@font-face/g) || []).length
  };
  
  console.log('📊 Critical CSS Stats:');
  console.log(`   Size: ${stats.totalSize} bytes (${(stats.totalSize / 1024).toFixed(2)} KB)`);
  console.log(`   Rules: ${stats.rules}`);
  console.log(`   Selectors: ${stats.selectors}`);
  console.log(`   Media queries: ${stats.mediaQueries}`);
  console.log(`   Font faces: ${stats.fontFaces}`);
  
  // Write stats to JSON
  const statsFile = path.join(BUILD_DIR, 'critical-stats.json');
  fs.writeFileSync(statsFile, JSON.stringify(stats, null, 2));
}

// Inline critical CSS in HTML files
async function inlineCriticalCSS() {
  console.log('💉 Inlining critical CSS...');
  
  const criticalCSS = fs.readFileSync(CRITICAL_CSS_FILE, 'utf8');
  const indexPath = path.join(BUILD_DIR, 'index.html');
  
  if (!fs.existsSync(indexPath)) {
    console.error('❌ index.html not found in build directory');
    return;
  }
  
  let html = fs.readFileSync(indexPath, 'utf8');
  
  // Remove existing critical CSS if present
  html = html.replace(/<style id="critical-css">[\s\S]*?<\/style>/, '');
  
  // Inline critical CSS in the head
  const criticalStyleTag = `<style id="critical-css">${criticalCSS}</style>`;
  html = html.replace('</head>', `  ${criticalStyleTag}\n</head>`);
  
  // Add preload hints for non-critical CSS
  const preloadHints = `
  <link rel="preload" href="/static/css/main.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
  <noscript><link rel="stylesheet" href="/static/css/main.css"></noscript>`;
  
  html = html.replace('</head>', `  ${preloadHints}\n</head>`);
  
  // Write updated HTML
  fs.writeFileSync(indexPath, html);
  console.log('✅ Critical CSS inlined successfully');
}

// Generate critical CSS loading script
function generateCriticalLoader() {
  const loaderScript = `
// Critical CSS loader with fallback
(function() {
  function loadCSS(href, before, media) {
    var doc = window.document;
    var ss = doc.createElement("link");
    var ref;
    if (before) {
      ref = before;
    } else {
      var refs = (doc.body || doc.getElementsByTagName("head")[0]).childNodes;
      ref = refs[refs.length - 1];
    }
    var sheets = doc.styleSheets;
    ss.rel = "stylesheet";
    ss.href = href;
    ss.media = "only x";
    
    function ready(cb) {
      if (doc.body) {
        return cb();
      }
      setTimeout(function() {
        ready(cb);
      });
    }
    
    ready(function() {
      ref.parentNode.insertBefore(ss, (before ? ref : ref.nextSibling));
    });
    
    var onloadcssdefined = function(cb) {
      var resolvedHref = ss.href;
      var i = sheets.length;
      while (i--) {
        if (sheets[i].href === resolvedHref) {
          return cb();
        }
      }
      setTimeout(function() {
        onloadcssdefined(cb);
      });
    };
    
    function loadCB() {
      if (ss.addEventListener) {
        ss.removeEventListener("load", loadCB);
      }
      ss.media = media || "all";
    }
    
    if (ss.addEventListener) {
      ss.addEventListener("load", loadCB);
    }
    ss.onloadcssdefined = onloadcssdefined;
    onloadcssdefined(loadCB);
    
    return ss;
  }
  
  // Load non-critical CSS asynchronously
  loadCSS("/static/css/main.css");
})();
  `;
  
  const loaderFile = path.join(BUILD_DIR, 'css-loader.js');
  fs.writeFileSync(loaderFile, loaderScript.trim());
  console.log('📜 CSS loader script generated');
}

// Main execution
async function main() {
  console.log('🚀 Starting critical CSS optimization...');
  
  try {
    // Check if build directory exists
    if (!fs.existsSync(BUILD_DIR)) {
      console.error('❌ Build directory not found. Please run "npm run build" first.');
      process.exit(1);
    }
    
    // Extract critical CSS
    await extractCriticalCSS();
    
    // Inline critical CSS
    await inlineCriticalCSS();
    
    // Generate CSS loader
    generateCriticalLoader();
    
    console.log('🎉 Critical CSS optimization completed successfully!');
    
  } catch (error) {
    console.error('❌ Critical CSS optimization failed:', error);
    process.exit(1);
  }
}

// Run if called directly
if (require.main === module) {
  main();
}

module.exports = {
  extractCriticalCSS,
  inlineCriticalCSS,
  generateCriticalLoader
};
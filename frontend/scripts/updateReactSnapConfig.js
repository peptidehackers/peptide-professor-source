#!/usr/bin/env node

/**
 * Update React Snap Configuration
 * Updates package.json with all generated static routes
 */

const fs = require('fs');
const path = require('path');

// Load generated routes
const routesFile = path.join(__dirname, 'staticRoutes.js');
const routes = require(routesFile);

// Load package.json
const packagePath = path.join(__dirname, '../package.json');
const packageContent = JSON.parse(fs.readFileSync(packagePath, 'utf8'));

// Update reactSnap configuration with all routes
packageContent.reactSnap = {
  ...packageContent.reactSnap,
  include: routes,
  source: "build",
  minifyHtml: {
    collapseWhitespace: true,
    removeComments: true,
    removeRedundantAttributes: true,
    removeScriptTypeAttributes: true,
    removeStyleLinkTypeAttributes: true,
    useShortDoctype: true
  },
  puppeteerArgs: [
    "--no-sandbox",
    "--disable-setuid-sandbox",
    "--disable-dev-shm-usage",
    "--disable-gpu",
    "--disable-background-timer-throttling",
    "--disable-backgrounding-occluded-windows",
    "--disable-renderer-backgrounding"
  ],
  skipThirdPartyRequests: true,
  removeBlobs: true,
  fixWebpackChunksIssue: "CRA2",
  concurrency: 4,
  crawl: true,
  waitFor: "networkidle0",
  timeout: 45000,
  userAgent: "ReactSnap",
  viewport: {
    width: 1280,
    height: 720
  }
};

// Write updated package.json
fs.writeFileSync(packagePath, JSON.stringify(packageContent, null, 2));

console.log(`✅ Updated react-snap configuration with ${routes.length} routes`);
console.log(`📄 Configuration saved to package.json`);
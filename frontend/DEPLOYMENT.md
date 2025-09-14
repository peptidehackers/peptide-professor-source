# Professor Peptides - Production Deployment Guide

## Overview

This document provides comprehensive deployment instructions for the Professor Peptides website across multiple static hosting platforms. The site is optimized for maximum performance with production-ready configurations for Vercel, Netlify, CloudFlare Pages, and GitHub Pages.

## 🚀 Quick Start

### Prerequisites

- Node.js 18+ and npm
- Git
- Platform CLI tools (optional but recommended)

### Build and Deploy

```bash
# Clone repository
git clone <repository-url>
cd frontend

# Install dependencies
npm ci

# Build for production
npm run build

# Deploy to your preferred platform
./scripts/deployment/deploy.sh vercel production
```

## 📋 Platform Configurations

### 🔷 Vercel (Primary Recommendation)

**Why Vercel?**
- Optimized for React applications
- Automatic deployments from Git
- Excellent performance and CDN
- Built-in analytics and monitoring

**Setup:**
1. Connect GitHub repository to Vercel
2. Configure environment variables
3. Deploy automatically on Git push

**Configuration Files:**
- `/vercel.json` - Build settings, headers, redirects
- `.env.production` - Production environment variables

**Environment Variables:**
```
REACT_APP_ENV=production
REACT_APP_BACKEND_URL=https://api.professorpeptides.org
REACT_APP_ANALYTICS_ID=G-XXXXXXXXXX
```

**Commands:**
```bash
# Install Vercel CLI
npm install -g vercel

# Deploy
vercel --prod

# Or use deployment script
./scripts/deployment/deploy.sh vercel production
```

### 🟢 Netlify (Alternative with Advanced Features)

**Why Netlify?**
- Advanced build processing
- Form handling capabilities
- Comprehensive plugin ecosystem
- Edge functions support

**Setup:**
1. Connect GitHub repository to Netlify
2. Configure build settings in netlify.toml
3. Set environment variables in dashboard

**Configuration Files:**
- `/netlify.toml` - Build settings, headers, redirects, plugins
- `.env.production` - Production environment variables

**Build Settings:**
- Build command: `npm run build`
- Publish directory: `build`
- Node version: 18

**Commands:**
```bash
# Install Netlify CLI
npm install -g netlify-cli

# Deploy
netlify deploy --prod --dir=build

# Or use deployment script
./scripts/deployment/deploy.sh netlify production
```

### ☁️ CloudFlare Pages (Global CDN)

**Why CloudFlare Pages?**
- Global edge network
- Excellent performance
- Free SSL and security features
- Worker functions support

**Setup:**
1. Connect GitHub repository to CloudFlare Pages
2. Configure build settings
3. Set environment variables

**Configuration Files:**
- `/wrangler.toml` - CloudFlare Workers configuration
- `/_headers` - Custom headers
- `/_redirects` - URL redirects

**Build Settings:**
- Build command: `npm run build`
- Build output directory: `build`
- Root directory: `/`

**Commands:**
```bash
# Install Wrangler CLI
npm install -g wrangler

# Deploy
wrangler pages publish build --project-name=professor-peptides

# Or use deployment script
./scripts/deployment/deploy.sh cloudflare production
```

### 🐙 GitHub Pages (Backup Option)

**Why GitHub Pages?**
- Free hosting for public repositories
- Simple setup
- Integrated with GitHub Actions

**Setup:**
1. Enable GitHub Pages in repository settings
2. Configure GitHub Actions workflow
3. Push to main branch to deploy

**Configuration Files:**
- `/.github/workflows/github-pages.yml` - CI/CD workflow
- `/.github/workflows/ci.yml` - Continuous integration

**Commands:**
```bash
# Deploy using GitHub CLI
gh workflow run github-pages.yml

# Or use deployment script
./scripts/deployment/deploy.sh github-pages production
```

## 🌍 Environment Management

### Environment Files

```
.env                    # Local development
.env.production        # Production environment
.env.staging          # Staging environment
.env.example          # Template file
```

### Environment Variables

| Variable | Production | Staging | Development |
|----------|------------|---------|-------------|
| `REACT_APP_ENV` | production | staging | development |
| `REACT_APP_BACKEND_URL` | https://api.professorpeptides.org | https://staging-api.professorpeptides.org | http://localhost:8001 |
| `REACT_APP_CDN_URL` | https://cdn.professorpeptides.org | https://staging-cdn.professorpeptides.org | - |
| `REACT_APP_ANALYTICS_ID` | G-XXXXXXXXXX | G-STAGING-XXXX | - |
| `GENERATE_SOURCEMAP` | false | true | true |

### Setting Environment Variables

**Vercel:**
```bash
vercel env add REACT_APP_BACKEND_URL production
```

**Netlify:**
```bash
netlify env:set REACT_APP_BACKEND_URL https://api.professorpeptides.org
```

**GitHub Actions:**
Set in repository Settings > Secrets and variables > Actions

## 🔄 CI/CD Pipeline

### GitHub Actions Workflows

1. **CI Pipeline** (`.github/workflows/ci.yml`)
   - Runs on all pushes and PRs
   - Tests, linting, security checks
   - Multi-platform builds

2. **Production Deployment** (`.github/workflows/github-pages.yml`)
   - Deploys to GitHub Pages on main branch
   - Includes build optimization

3. **Staging Deployment** (`.github/workflows/deploy-staging.yml`)
   - Deploys to staging on develop branch
   - Includes E2E testing

### Pipeline Features

- **Automated Testing**: Unit tests, E2E tests, security scans
- **Code Quality**: ESLint, Prettier, code coverage
- **Performance**: Lighthouse CI, bundle analysis
- **Security**: Dependency scanning, vulnerability checks
- **Notifications**: Slack/Discord integration

## 📊 Monitoring and Analytics

### Performance Monitoring

**Lighthouse CI:**
- Automated performance audits
- Core Web Vitals tracking
- Performance budgets enforcement

**Vercel Analytics:**
- Real User Monitoring (RUM)
- Performance insights
- User behavior tracking

### Error Tracking

**Sentry Integration:**
```javascript
// Environment: production
REACT_APP_SENTRY_DSN=https://...@sentry.io/...
```

### Health Checks

**Automated Monitoring:**
```bash
# Run health checks
./scripts/deployment/health-check.sh production
```

**Monitored Endpoints:**
- `/` - Homepage
- `/calculators` - Tools page
- `/peptides/browse` - Browse page
- `/sitemap.xml` - SEO
- `/robots.txt` - SEO
- `/manifest.json` - PWA

## 🛡️ Security Configuration

### Headers

All platforms configured with security headers:
- `Strict-Transport-Security`
- `X-Content-Type-Options`
- `X-Frame-Options`
- `Content-Security-Policy`
- `Referrer-Policy`
- `Permissions-Policy`

### SSL/HTTPS

- All platforms provide automatic SSL certificates
- HTTPS enforced via security headers
- Certificate monitoring included

## 🎯 Performance Optimization

### Build Optimization

- **Code Splitting**: Automatic route-based splitting
- **Tree Shaking**: Dead code elimination
- **Minification**: JavaScript and CSS compression
- **Source Maps**: Disabled in production

### Caching Strategy

- **Static Assets**: 1 year cache (`max-age=31536000`)
- **HTML**: No cache for SPA routing
- **API Responses**: Custom cache headers
- **Fonts/Images**: Immutable caching

### CDN Configuration

- **Global Distribution**: Edge locations worldwide
- **Asset Optimization**: Automatic image optimization
- **Brotli Compression**: Better than gzip
- **HTTP/2**: Multiplexed connections

## 🔧 Deployment Scripts

### Main Deployment Script

```bash
./scripts/deployment/deploy.sh [platform] [environment]
```

**Platforms:** `vercel`, `netlify`, `cloudflare`, `github-pages`, `all`
**Environments:** `production`, `staging`, `development`

**Features:**
- Dependency checking
- Automated testing
- Build optimization
- Multi-platform deployment
- Performance auditing
- Notification integration

### Health Check Script

```bash
./scripts/deployment/health-check.sh [environment]
```

**Checks:**
- Endpoint availability
- SSL certificate validity
- DNS resolution
- Core Web Vitals
- Response times

## 📈 Performance Budgets

### Lighthouse Thresholds

- **Performance**: ≥85
- **Accessibility**: ≥90
- **Best Practices**: ≥90
- **SEO**: ≥90
- **PWA**: ≥80

### Resource Budgets

- **JavaScript Bundle**: ≤500KB
- **CSS Bundle**: ≤100KB
- **Images**: ≤1MB
- **Total Size**: ≤2MB

### Core Web Vitals

- **LCP**: ≤2.5s
- **FID**: ≤100ms
- **CLS**: ≤0.1

## 🚨 Troubleshooting

### Common Issues

**Build Failures:**
1. Check Node.js version (18+ required)
2. Clear node_modules and reinstall
3. Verify environment variables

**Deployment Errors:**
1. Check platform-specific logs
2. Verify authentication tokens
3. Review configuration files

**Performance Issues:**
1. Run Lighthouse audit
2. Check bundle analysis
3. Review caching headers

### Debug Commands

```bash
# Check build locally
npm run build && npx serve build

# Analyze bundle size
npm install -g webpack-bundle-analyzer
npx webpack-bundle-analyzer build/static/js/*.js

# Test production build
NODE_ENV=production npm run build
```

## 📞 Support and Maintenance

### Regular Tasks

- **Weekly**: Review performance metrics
- **Monthly**: Update dependencies
- **Quarterly**: Security audit
- **Annually**: Platform evaluation

### Monitoring Dashboards

- **Vercel**: Real-time performance metrics
- **Netlify**: Build and deploy logs
- **CloudFlare**: Analytics and security
- **GitHub**: Actions and repository insights

### Contact Information

- **Technical Lead**: [Contact information]
- **DevOps Team**: [Contact information]
- **Emergency Contact**: [Contact information]

## 📚 Additional Resources

- [React Deployment Guide](https://create-react-app.dev/docs/deployment/)
- [Vercel Documentation](https://vercel.com/docs)
- [Netlify Documentation](https://docs.netlify.com/)
- [CloudFlare Pages Documentation](https://developers.cloudflare.com/pages/)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)

---

*Last updated: $(date +'%Y-%m-%d')*
*Version: 1.0.0*
// Monitoring and Analytics Configuration
const MonitoringConfig = {
  // Analytics Configuration
  analytics: {
    google: {
      measurementId: process.env.REACT_APP_GA_MEASUREMENT_ID || 'G-XXXXXXXXXX',
      enabled: process.env.NODE_ENV === 'production'
    },
    vercel: {
      enabled: process.env.VERCEL || false
    },
    plausible: {
      domain: 'professorpeptides.org',
      enabled: process.env.REACT_APP_PLAUSIBLE_ENABLED === 'true'
    }
  },

  // Error Tracking
  errorTracking: {
    sentry: {
      dsn: process.env.REACT_APP_SENTRY_DSN,
      environment: process.env.REACT_APP_ENV || 'development',
      enabled: !!process.env.REACT_APP_SENTRY_DSN,
      tracesSampleRate: process.env.NODE_ENV === 'production' ? 0.1 : 1.0,
      beforeSend: (event) => {
        // Filter out non-critical errors in production
        if (process.env.NODE_ENV === 'production' && event.level === 'warning') {
          return null;
        }
        return event;
      }
    },
    logRocket: {
      appId: process.env.REACT_APP_LOGROCKET_APP_ID,
      enabled: !!process.env.REACT_APP_LOGROCKET_APP_ID && process.env.NODE_ENV === 'production'
    }
  },

  // Performance Monitoring
  performance: {
    webVitals: {
      enabled: true,
      reportToAnalytics: true,
      thresholds: {
        fcp: 1800,
        lcp: 2500,
        fid: 100,
        cls: 0.1,
        ttfb: 600
      }
    },
    lighthouse: {
      budgets: {
        performance: 85,
        accessibility: 90,
        bestPractices: 90,
        seo: 90,
        pwa: 80
      }
    }
  },

  // Real User Monitoring (RUM)
  rum: {
    enabled: process.env.NODE_ENV === 'production',
    sampleRate: 0.1, // 10% of users
    trackingConfig: {
      pageViews: true,
      userInteractions: true,
      errors: true,
      performance: true,
      customEvents: true
    }
  },

  // Health Checks
  healthChecks: {
    interval: 300000, // 5 minutes
    endpoints: [
      '/health',
      '/api/health',
      '/sitemap.xml',
      '/robots.txt'
    ],
    alerting: {
      enabled: process.env.NODE_ENV === 'production',
      webhooks: process.env.REACT_APP_ALERT_WEBHOOKS?.split(',') || []
    }
  },

  // Feature Flags
  featureFlags: {
    newCalculatorUI: process.env.REACT_APP_FF_NEW_CALCULATOR_UI === 'true',
    advancedAnalytics: process.env.REACT_APP_FF_ADVANCED_ANALYTICS === 'true',
    betaFeatures: process.env.REACT_APP_FF_BETA_FEATURES === 'true'
  }
};

export default MonitoringConfig;
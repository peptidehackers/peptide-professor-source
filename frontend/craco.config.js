const path = require('path');
const CompressionPlugin = require('compression-webpack-plugin');
const TerserPlugin = require('terser-webpack-plugin');
const { BundleAnalyzerPlugin } = require('webpack-bundle-analyzer');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const PreloadWebpackPlugin = require('preload-webpack-plugin');

const securityHeaders = [
  { key: 'Strict-Transport-Security', value: 'max-age=31536000; includeSubDomains; preload' },
  { key: 'X-Content-Type-Options', value: 'nosniff' },
  { key: 'X-Frame-Options', value: 'DENY' },
  { key: 'Referrer-Policy', value: 'strict-origin-when-cross-origin' },
  { key: 'Permissions-Policy', value: 'camera=(), microphone=(), geolocation=()' },
  { key: 'Content-Security-Policy', value: "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; img-src 'self' data: https:; connect-src 'self' https:; frame-ancestors 'none'" }
];

module.exports = {
  productionBrowserSourceMaps: false,
  
  webpack: {
    configure: (webpackConfig, { env, paths }) => {
      // Production optimizations
      if (env === 'production') {
        // Advanced code splitting
        webpackConfig.optimization = {
          ...webpackConfig.optimization,
          splitChunks: {
            chunks: 'all',
            cacheGroups: {
              // Vendor chunk for third-party libraries
              vendor: {
                test: /[\\/]node_modules[\\/]/,
                name: 'vendors',
                chunks: 'all',
                priority: 10,
                reuseExistingChunk: true,
              },
              // React chunk
              react: {
                test: /[\\/]node_modules[\\/](react|react-dom)[\\/]/,
                name: 'react',
                chunks: 'all',
                priority: 20,
                reuseExistingChunk: true,
              },
              // Common chunk for shared components
              common: {
                name: 'common',
                minChunks: 2,
                chunks: 'all',
                priority: 5,
                reuseExistingChunk: true,
                enforce: true,
              },
              // CSS chunk
              styles: {
                name: 'styles',
                test: /\.css$/,
                chunks: 'all',
                enforce: true,
                priority: 15,
              }
            }
          },
          // Advanced minification
          minimizer: [
            new TerserPlugin({
              terserOptions: {
                parse: {
                  ecma: 8,
                },
                compress: {
                  ecma: 5,
                  warnings: false,
                  comparisons: false,
                  inline: 2,
                  drop_console: true,
                  drop_debugger: true,
                  pure_funcs: ['console.log', 'console.info', 'console.debug'],
                },
                mangle: {
                  safari10: true,
                },
                output: {
                  ecma: 5,
                  comments: false,
                  ascii_only: true,
                },
              },
              parallel: true,
            }),
          ],
          // Module concatenation
          concatenateModules: true,
          // Tree shaking
          usedExports: true,
          sideEffects: false,
        };

        // Advanced compression
        webpackConfig.plugins.push(
          new CompressionPlugin({
            filename: '[path][base].gz',
            algorithm: 'gzip',
            test: /\.(js|css|html|svg)$/,
            threshold: 8192,
            minRatio: 0.8,
          }),
          new CompressionPlugin({
            filename: '[path][base].br',
            algorithm: 'brotliCompress',
            test: /\.(js|css|html|svg)$/,
            compressionOptions: {
              level: 11,
            },
            threshold: 8192,
            minRatio: 0.8,
          })
        );

        // Bundle analyzer (only if ANALYZE=true)
        if (process.env.ANALYZE) {
          webpackConfig.plugins.push(
            new BundleAnalyzerPlugin({
              analyzerMode: 'static',
              openAnalyzer: false,
            })
          );
        }

        // Preload critical resources
        webpackConfig.plugins.push(
          new PreloadWebpackPlugin({
            rel: 'preload',
            include: 'initial',
            fileBlacklist: [/\.map$/, /hot-update\.js$/]
          })
        );

        // Performance hints
        webpackConfig.performance = {
          hints: 'warning',
          maxEntrypointSize: 250000,
          maxAssetSize: 250000,
        };

        // Module resolution optimizations
        webpackConfig.resolve = {
          ...webpackConfig.resolve,
          alias: {
            ...webpackConfig.resolve.alias,
            '@': path.resolve(__dirname, 'src'),
            'components': path.resolve(__dirname, 'src/components'),
            'pages': path.resolve(__dirname, 'src/pages'),
            'utils': path.resolve(__dirname, 'src/utils'),
            'styles': path.resolve(__dirname, 'src/styles'),
          },
          extensions: ['.js', '.jsx', '.ts', '.tsx', '.json'],
        };
      }

      return webpackConfig;
    }
  },

  // PostCSS optimizations
  style: {
    postcss: {
      plugins: [
        require('postcss-preset-env')({
          stage: 3,
          features: {
            'custom-properties': false,
          },
        }),
        require('cssnano')({
          preset: ['default', {
            discardComments: { removeAll: true },
            normalizeWhitespace: true,
            minifyFontValues: true,
            minifySelectors: true,
          }]
        })
      ]
    }
  },

  async headers() {
    return [
      { source: '/(.*)', headers: securityHeaders }
    ];
  }
};
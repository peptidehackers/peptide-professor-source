// Advanced Service Worker for Professor Peptides - Performance Optimized

const CACHE_VERSION = '2.0.0';
const CACHE_NAME = `professor-peptides-v${CACHE_VERSION}`;
const STATIC_CACHE = `static-v${CACHE_VERSION}`;
const RUNTIME_CACHE = `runtime-v${CACHE_VERSION}`;
const IMAGE_CACHE = `images-v${CACHE_VERSION}`;

// Critical resources to cache immediately (precache)
const CRITICAL_ASSETS = [
  '/',
  '/static/css/main.css',
  '/static/js/main.js',
  '/manifest.json',
  '/favicon.ico',
  '/robots.txt'
];

// Network-first strategy for dynamic content (fresh data preferred)
const NETWORK_FIRST = [
  '/api/',
  '/calculators/',
  '/peptides/',
  '/research/',
  '/blog/',
  '/quiz-results'
];

// Cache-first strategy for static assets (performance first)
const CACHE_FIRST = [
  '/static/',
  '/icons/',
  '/images/',
  '/locales/',
  '.woff2',
  '.woff',
  '.ttf'
];

// Stale-while-revalidate for frequently updated content
const STALE_WHILE_REVALIDATE = [
  '/about',
  '/faq',
  '/resources'
];

// Cache duration configurations
const CACHE_DURATIONS = {
  images: 30 * 24 * 60 * 60 * 1000, // 30 days
  static: 365 * 24 * 60 * 60 * 1000, // 1 year
  runtime: 24 * 60 * 60 * 1000, // 1 day
  api: 5 * 60 * 1000 // 5 minutes
};

// Install event - precache critical assets
self.addEventListener('install', event => {
  console.log('[SW] Install event');
  
  event.waitUntil(
    Promise.all([
      // Precache critical assets
      caches.open(CACHE_NAME).then(cache => {
        console.log('[SW] Precaching critical assets');
        return cache.addAll(CRITICAL_ASSETS);
      }),
      
      // Skip waiting to activate immediately
      self.skipWaiting()
    ])
  );
});

// Activate event - clean old caches and take control
self.addEventListener('activate', event => {
  console.log('[SW] Activate event');
  
  event.waitUntil(
    Promise.all([
      // Clean up old caches
      caches.keys().then(cacheNames => {
        return Promise.all(
          cacheNames
            .filter(cacheName => 
              !cacheName.includes(CACHE_VERSION) && 
              cacheName.startsWith('professor-peptides-')
            )
            .map(cacheName => {
              console.log('[SW] Deleting old cache:', cacheName);
              return caches.delete(cacheName);
            })
        );
      }),
      
      // Take control of all clients
      self.clients.claim()
    ])
  );
});

// Fetch event - implement intelligent caching strategies
self.addEventListener('fetch', event => {
  const { request } = event;
  const url = new URL(request.url);
  
  // Skip non-GET requests and chrome-extension requests
  if (request.method !== 'GET' || url.protocol === 'chrome-extension:') {
    return;
  }
  
  // Handle different request types with specific strategies
  if (isImageRequest(request)) {
    event.respondWith(handleImageRequest(request));
  } else if (isStaticAsset(request)) {
    event.respondWith(handleStaticAsset(request));
  } else if (isAPIRequest(request)) {
    event.respondWith(handleAPIRequest(request));
  } else if (isNavigationRequest(request)) {
    event.respondWith(handleNavigationRequest(request));
  } else {
    event.respondWith(handleGenericRequest(request));
  }
});

// Check if request is for an image
function isImageRequest(request) {
  return request.destination === 'image' || 
         /\.(jpg|jpeg|png|gif|webp|svg|ico)$/i.test(new URL(request.url).pathname);
}

// Check if request is for a static asset
function isStaticAsset(request) {
  const url = new URL(request.url);
  return CACHE_FIRST.some(path => 
    url.pathname.startsWith(path) || url.pathname.includes(path)
  );
}

// Check if request is for API
function isAPIRequest(request) {
  const url = new URL(request.url);
  return NETWORK_FIRST.some(path => url.pathname.startsWith(path));
}

// Check if request is for navigation
function isNavigationRequest(request) {
  return request.mode === 'navigate' || 
         (request.method === 'GET' && request.headers.get('accept').includes('text/html'));
}

// Handle image requests with cache-first + expiration
async function handleImageRequest(request) {
  const cache = await caches.open(IMAGE_CACHE);
  const cached = await cache.match(request);
  
  if (cached) {
    const cachedDate = new Date(cached.headers.get('date'));
    const now = new Date();
    
    // Serve from cache if within expiration
    if (now.getTime() - cachedDate.getTime() < CACHE_DURATIONS.images) {
      return cached;
    }
  }
  
  try {
    const response = await fetch(request);
    
    if (response.ok && response.status < 400) {
      const responseClone = response.clone();
      
      // Add timestamp header for expiration tracking
      const headers = new Headers(responseClone.headers);
      headers.set('date', new Date().toISOString());
      
      const modifiedResponse = new Response(responseClone.body, {
        status: responseClone.status,
        statusText: responseClone.statusText,
        headers: headers
      });
      
      cache.put(request, modifiedResponse);
    }
    
    return response;
  } catch (error) {
    // Return cached version if network fails
    if (cached) {
      return cached;
    }
    throw error;
  }
}

// Handle static assets with cache-first strategy
async function handleStaticAsset(request) {
  const cache = await caches.open(STATIC_CACHE);
  const cached = await cache.match(request);
  
  if (cached) {
    return cached;
  }
  
  try {
    const response = await fetch(request);
    
    if (response.ok && response.status < 400) {
      const responseClone = response.clone();
      cache.put(request, responseClone);
    }
    
    return response;
  } catch (error) {
    console.log('[SW] Static asset fetch failed:', request.url);
    throw error;
  }
}

// Handle API requests with network-first strategy
async function handleAPIRequest(request) {
  const cache = await caches.open(RUNTIME_CACHE);
  
  try {
    const response = await fetch(request);
    
    if (response.ok && response.status < 400) {
      const responseClone = response.clone();
      
      // Cache with expiration metadata
      const headers = new Headers(responseClone.headers);
      headers.set('sw-cache-timestamp', Date.now().toString());
      
      const modifiedResponse = new Response(responseClone.body, {
        status: responseClone.status,
        statusText: responseClone.statusText,
        headers: headers
      });
      
      cache.put(request, modifiedResponse);
    }
    
    return response;
  } catch (error) {
    const cached = await cache.match(request);
    
    if (cached) {
      const cacheTimestamp = parseInt(cached.headers.get('sw-cache-timestamp')) || 0;
      const now = Date.now();
      
      // Only return cached API data if it's recent
      if (now - cacheTimestamp < CACHE_DURATIONS.api) {
        return cached;
      }
    }
    
    throw error;
  }
}

// Handle navigation requests with network-first + offline fallback
async function handleNavigationRequest(request) {
  try {
    const response = await fetch(request);
    
    if (response.ok) {
      const cache = await caches.open(RUNTIME_CACHE);
      cache.put(request, response.clone());
    }
    
    return response;
  } catch (error) {
    const cache = await caches.open(CACHE_NAME);
    const cached = await cache.match('/');
    
    if (cached) {
      return cached;
    }
    
    // Return offline page if available
    return cache.match('/offline.html') || new Response(
      'Offline - Please check your internet connection',
      { headers: { 'Content-Type': 'text/html' } }
    );
  }
}

// Handle generic requests with stale-while-revalidate
async function handleGenericRequest(request) {
  const cache = await caches.open(RUNTIME_CACHE);
  const cached = await cache.match(request);
  
  const fetchPromise = fetch(request).then(response => {
    if (response.ok && response.status < 400) {
      const responseClone = response.clone();
      cache.put(request, responseClone);
    }
    return response;
  }).catch(() => null);
  
  // Return cached immediately if available, otherwise wait for network
  return cached || fetchPromise;
}

// Background sync for offline functionality
self.addEventListener('sync', event => {
  console.log('[SW] Background sync event:', event.tag);
  
  if (event.tag === 'peptide-data-sync') {
    event.waitUntil(syncPeptideData());
  } else if (event.tag === 'calculator-sync') {
    event.waitUntil(syncCalculatorData());
  }
});

// Sync peptide data in background
async function syncPeptideData() {
  try {
    const response = await fetch('/api/peptides');
    if (response.ok) {
      const cache = await caches.open(RUNTIME_CACHE);
      cache.put('/api/peptides', response.clone());
      console.log('[SW] Peptide data synced successfully');
    }
  } catch (error) {
    console.log('[SW] Failed to sync peptide data:', error);
  }
}

// Sync calculator data in background
async function syncCalculatorData() {
  try {
    const calculatorEndpoints = [
      '/api/calculators/bmi',
      '/api/calculators/glp1',
      '/api/calculators/trt'
    ];
    
    await Promise.all(
      calculatorEndpoints.map(async endpoint => {
        const response = await fetch(endpoint);
        if (response.ok) {
          const cache = await caches.open(RUNTIME_CACHE);
          cache.put(endpoint, response.clone());
        }
      })
    );
    
    console.log('[SW] Calculator data synced successfully');
  } catch (error) {
    console.log('[SW] Failed to sync calculator data:', error);
  }
}

// Push notification handling
self.addEventListener('push', event => {
  const options = {
    body: 'New peptide research available!',
    icon: '/icons/icon-192x192.png',
    badge: '/icons/badge-72x72.png',
    vibrate: [100, 50, 100],
    data: {
      dateOfArrival: Date.now(),
      primaryKey: 1
    },
    actions: [
      {
        action: 'explore',
        title: 'Explore Research',
        icon: '/icons/checkmark.png'
      },
      {
        action: 'close',
        title: 'Close',
        icon: '/icons/xmark.png'
      }
    ]
  };
  
  event.waitUntil(
    self.registration.showNotification('Professor Peptides', options)
  );
});

// Notification click handling
self.addEventListener('notificationclick', event => {
  event.notification.close();
  
  if (event.action === 'explore') {
    event.waitUntil(
      clients.openWindow('/research')
    );
  }
});

// Message handling from main thread
self.addEventListener('message', event => {
  if (event.data && event.data.type === 'SKIP_WAITING') {
    self.skipWaiting();
  } else if (event.data && event.data.type === 'CACHE_UPDATE') {
    // Force update specific cache entries
    event.waitUntil(updateCache(event.data.urls));
  }
});

// Update specific cache entries
async function updateCache(urls) {
  const cache = await caches.open(RUNTIME_CACHE);
  
  await Promise.all(
    urls.map(async url => {
      try {
        const response = await fetch(url);
        if (response.ok) {
          cache.put(url, response.clone());
        }
      } catch (error) {
        console.log('[SW] Failed to update cache for:', url);
      }
    })
  );
}

// Periodic background sync (if supported)
if ('periodicSync' in self.registration) {
  self.addEventListener('periodicsync', event => {
    if (event.tag === 'peptide-data-refresh') {
      event.waitUntil(syncPeptideData());
    }
  });
}

console.log('[SW] Advanced Service Worker initialized');
const CACHE_NAME = "blockrunner-v18";

const FILES_TO_CACHE = [
  "./",
  "./index.html",
  "./manifest.json",
  "./icons/icon.png",
  "./icons/icon.ico",
  "./music/game.mp3",
  "./music/menu.mp3",
  "./favicon.png",
  "./apple-icon.png",
  // додай тут інші файли гри (звуки, картинки, рівні)
];

// Встановлення кешу
self.addEventListener("install", event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      return cache.addAll(FILES_TO_CACHE);
    })
  );
  self.skipWaiting();
});

// Активування нового service worker
self.addEventListener("activate", event => {
  event.waitUntil(
    caches.keys().then(keys => {
      return Promise.all(
        keys
          .filter(key => key !== CACHE_NAME)
          .map(key => caches.delete(key))
      );
    })
  );
  self.clients.claim();
});

// Обробка запитів (офлайн режим)
self.addEventListener("fetch", event => {
  event.respondWith(
    caches.match(event.request).then(cached => {
      return cached || fetch(event.request);
    })
  );
});

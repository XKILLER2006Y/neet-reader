/* Offline shell: app + question bank cached. NCERT PDFs stay network (official site). */
const CACHE='neet-reader-v1';
const CORE=['./','./index.html','./manifest.json'];
self.addEventListener('install',e=>{
  e.waitUntil(caches.open(CACHE).then(async c=>{
    await c.addAll(CORE);
    try{
      const r=await fetch('./questions/manifest.json');
      if(r.ok){const files=await r.json();await c.addAll(files.map(f=>'./questions/'+f));}
    }catch{}
  }).then(()=>self.skipWaiting()));
});
self.addEventListener('activate',e=>{
  e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim()));
});
self.addEventListener('fetch',e=>{
  const u=new URL(e.request.url);
  if(u.hostname==='ncert.nic.in'){return;} // official PDFs always live
  e.respondWith(caches.match(e.request).then(hit=>hit||fetch(e.request).then(res=>{
    if(e.request.method==='GET'&&res.ok){const cp=res.clone();caches.open(CACHE).then(c=>c.put(e.request,cp));}
    return res;
  }).catch(()=>caches.match('./index.html'))));
});

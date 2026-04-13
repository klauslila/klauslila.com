export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    // Proxy FR24 requests
    if (url.pathname === '/fr24') {
      const qs = url.search;
      const target = 'https://data-cloud.flightradar24.com/zones/fcgi/feed.js' + qs;

      try {
        const resp = await fetch(target, {
          headers: {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
            'Referer': 'https://www.flightradar24.com/',
            'Origin': 'https://www.flightradar24.com',
            'Accept': 'application/json, text/javascript, */*',
          },
        });

        return new Response(resp.body, {
          status: resp.status,
          headers: {
            'Content-Type': 'application/json',
            'Cache-Control': 'public, max-age=2',
            'Access-Control-Allow-Origin': '*',
          },
        });
      } catch (e) {
        return new Response(JSON.stringify({ error: e.message }), {
          status: 502,
          headers: { 'Content-Type': 'application/json' },
        });
      }
    }

    // Everything else: serve static assets
    return env.ASSETS.fetch(request);
  },
};

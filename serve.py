#!/usr/bin/env python3
"""Local dev server: static files + FR24 flight data proxy."""
import http.server
import urllib.request
import urllib.parse
import json

PORT = 8080

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/fr24?'):
            qs = self.path[6:]  # everything after /fr24?
            url = 'https://data-cloud.flightradar24.com/zones/fcgi/feed.js?' + qs
            try:
                req = urllib.request.Request(url, headers={
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
                    'Referer': 'https://www.flightradar24.com/',
                    'Origin': 'https://www.flightradar24.com',
                    'Accept': 'application/json, text/javascript, */*',
                })
                with urllib.request.urlopen(req, timeout=10) as resp:
                    data = resp.read()
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.send_header('Cache-Control', 'no-cache')
                self.end_headers()
                self.wfile.write(data)
            except Exception as e:
                self.send_response(502)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': str(e)}).encode())
            return

        super().do_GET()

    def log_message(self, format, *args):
        if '200' not in str(args):
            super().log_message(format, *args)

if __name__ == '__main__':
    with http.server.HTTPServer(('', PORT), Handler) as server:
        print(f'Serving at http://localhost:{PORT}')
        print('Press Ctrl+C to stop')
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print('\nStopped.')

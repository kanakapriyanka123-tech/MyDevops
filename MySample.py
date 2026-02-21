print("Hello..Devops")
from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8000

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"""
        <html>
            <head><title>My DevOps Page</title></head>
            <body>
                <h1>Hello from Jenkins CI 🚀</h1>
                <p>This page is served using Python.</p>
            </body>
        </html>
        """)

with HTTPServer(("", PORT), MyHandler) as server:
    print(f"Server running on port {PORT}")
    server.serve_forever()

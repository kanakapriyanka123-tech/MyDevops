print("Hello..Devops")
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 8000

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Send response status
        self.send_response(200)
        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # Send HTML content
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>My Simple Web Page</title>
        </head>
        <body>
            <h1>Welcome to My Web Page!</h1>
            <p>This page is served directly from Python without Flask or HTML files.</p>
        </body>
        </html>
        """
        self.wfile.write(html.encode('utf-8'))

# Start the server
with HTTPServer(('', PORT), MyHandler) as server:
    print(f"Server running at http://localhost:{PORT}")
    server.serve_forever()

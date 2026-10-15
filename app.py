from http.server import SimpleHTTPRequestHandler, HTTPServer

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        # This is the webpage message users will see
        self.wfile.write(b"<h1>DevOps Project 1: Hello, This is vijay from Docker!</h1>")

print("Server starting on port 8000...")
server = HTTPServer(("0.0.0.0", 8000), MyHandler)
server.serve_forever()

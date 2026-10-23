from http.server import SimpleHTTPRequestHandler, HTTPServer

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        # Define the multi-line HTML block correctly
        html_content = """
        <html>
        <head>
            <style>
                body { font-family: 'Segoe UI', Arial, sans-serif; margin: 40px; background-color: #f4f7f6; color: #333; }
                .container { max-width: 800px; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); }
                h1 { color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px; }
                p { line-height: 1.6; font-size: 16px; color: #555; text-align: justify; }
                .badge { background-color: #2ecc71; color: white; padding: 5px 10px; border-radius: 4px; font-size: 14px; font-weight: bold; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>DevOps Infrastructure Pipeline <span class="badge">Version 7.0 Ultra Live!!!
 
            
                <p><strong>Automated Continuous Delivery:</strong> This application serves as a living proof-of-concept for automated cloud infrastructure. Every single time a developer modifies this text layout locally and pushes it to version control, a GitHub Actions runner intercepts the event, stands up an isolated execution node, validates the application framework, and bakes the new changes securely into a production-ready package.</p>
                
                <p><strong>Containerized Architecture:</strong> By shifting away from heavy monolithic virtual machines toward lightweight Docker containers, we isolate process environments completely. This guarantees that the application runs identically on a local development laptop, a QA testing server, or a multi-node high-availability production cluster in the cloud without system configuration drift.</p>
                
                <p><strong>The SysAdmin Advantage:</strong> Transitioning from classic systems administration to DevOps means translating manual operational wisdom into software patterns. By utilizing robust build logic, secure secret masking keys, and standardized images, we construct digital assembly lines that reduce deployment times from hours down to seconds.</p>
            </div>
        </body>
        </html>
        """
        # Encode and send the clean block out to the browser
        self.wfile.write(html_content.encode('utf-8'))

print("Server starting on port 8000...")
server = HTTPServer(("0.0.0.0", 8000), MyHandler)
server.serve_forever()

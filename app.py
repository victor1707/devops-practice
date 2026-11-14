from http.server import BaseHTTPRequestHandler, HTTPServer
import os

VERSION = os.environ.get("APP_VERSION", "dev")

def message():
    return f"hello from devops-practice {VERSION}\n"

class H(BaseHTTPRequestHandler):
    def do_GET(self):
        body = (b"ok\n" if self.path == "/health" else message().encode())
        self.send_response(200); self.end_headers(); self.wfile.write(body)

if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8080), H).serve_forever()

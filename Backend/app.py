from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        client_ip, client_port = self.client_address

        body = (
            f"TCP peer: {client_ip}:{client_port}\n"
            f"\n"
            f"HTTP headers received by backend:\n"
            f"Host: {self.headers.get('Host')}\n"
            f"X-Real-IP: {self.headers.get('X-Real-IP')}\n"
            f"X-Forwarded-For: {self.headers.get('X-Forwarded-For')}\n"
            f"My-Test: {self.headers.get('My-Test')}\n"
        )

        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(body.encode())


HTTPServer(("0.0.0.0", 5000), Handler).serve_forever()
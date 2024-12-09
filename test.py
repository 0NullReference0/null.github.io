import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleAPIHandler(BaseHTTPRequestHandler):

    def _send_response(self, status_code, data=None):
        # Send HTTP response header
        self.send_response(status_code)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        
        if data:
            self.wfile.write(json.dumps(data).encode("utf-8"))

    def do_GET(self):
        """Handle GET requests"""
        if self.path == "/api/data":
            data = {"message": "This is a GET response from the API."}
            self._send_response(200, data)
        else:
            self._send_response(404, {"error": "Not found"})

    def do_POST(self):
        """Handle POST requests"""
        if self.path == "/api/data":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            try:
                json_data = json.loads(post_data)
                response_data = {"received_data": json_data}
                self._send_response(200, response_data)
            except json.JSONDecodeError:
                self._send_response(400, {"error": "Invalid JSON"})
        else:
            self._send_response(404, {"error": "Not found"})

    def do_PUT(self):
        """Handle PUT requests"""
        if self.path == "/api/data":
            content_length = int(self.headers['Content-Length'])
            put_data = self.rfile.read(content_length)
            try:
                json_data = json.loads(put_data)
                # Process PUT data (here, just echoing back)
                response_data = {"updated_data": json_data}
                self._send_response(200, response_data)
            except json.JSONDecodeError:
                self._send_response(400, {"error": "Invalid JSON"})
        else:
            self._send_response(404, {"error": "Not found"})

    def do_DELETE(self):
        """Handle DELETE requests"""
        if self.path == "/api/data":
            data = {"message": "Resource has been deleted."}
            self._send_response(200, data)
        else:
            self._send_response(404, {"error": "Not found"})

def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting simple API on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()

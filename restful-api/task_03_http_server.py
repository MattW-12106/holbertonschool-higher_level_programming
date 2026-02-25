#!/usr/bin/python3
"""Develop a simple API using Python with the `http.server` module"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleAPIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Handle GET requests"""

        # If the path is '/', return a welcome message
        if self.path == '/':
            message = b"Hello, this is a simple API!"
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.send_header('Content-Length', str(len(message)))
            self.end_headers()
            self.wfile.write(message)

        # If the path is '/data', return a JSON response with some data
        elif self.path == '/data':
            data = {"name": "John Doe", "age": 30, "city": "New York"}
            message = json.dumps(data, separators=(',', ':')).encode("utf-8")
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Content-Length', str(len(message)))
            self.end_headers()
            self.wfile.write(message)
        
        # If the path is '/status', return a plain text response with "OK"
        elif self.path == "/status":
            message = b"OK"
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.send_header('Content-Length', str(len(message)))
            self.end_headers()
            self.wfile.write(message)
        
        # If the path is not there, return a 404 Not Found response
        else:
            message = b"404 Not Found"
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.send_header('Content-Length', str(len(message)))
            self.end_headers()
            self.wfile.write(message)

# Run the HTTP server
if __name__ == "__main__":
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    httpd.serve_forever()
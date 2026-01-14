from http.server import BaseHTTPRequestHandler, HTTPServer
import time

a=0

class VulnerableHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global a
        # a long processing time (3 seconds)
        time.sleep(3)

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        st=str(a)
        self.wfile.write(bytes(f"Request processed. Count: {st}", "utf-8"))
        a=a+1


def run(server_class=HTTPServer, handler_class=VulnerableHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting vulnerable server on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
# -*- coding:utf-8 -*-
# Author: Jason Lee

from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            f = open(self.path[1:], 'r')
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(f.read())
            f.close()
        except Exception as e:
            self.send_error(404, 'Error: %s' % str(e))


def main():
    try:
        server = HTTPServer(('', 80), MyHandler)
        server.serve_forever()
    except Exception as e:
        print('the end...')
        server.socket.close()

if __name__ == '__main__':
    main()
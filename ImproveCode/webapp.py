# -*- coding:utf-8 -*-
# Author: Jason Lee
import pprint
from wsgiref.simple_server import make_server


def application(environ, start_response):
    pprint.pprint(environ)
    print('=' * 64)
    print(start_response)
    start_response('200 OK', [('Content-type', 'text/html')])
    return bytes('Hello, world!', encoding='utf-8')


server = make_server('', 7899, application)
server.serve_forever()

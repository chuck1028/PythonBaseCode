# _*_ coding: utf-8 _*_
from wsgiref.simple_server import make_server

def application(environ, start_response):
    #environ: 包含客户端所有请求信息
    #start_response: 设置响应头
    for k in environ:
        print k, ': ', environ[k]
    start_response('200 OK', [('Content-Type', 'text/html')])
    return 'Hello Web!'

httpd = make_server('', 8080, application)

httpd.serve_forever()

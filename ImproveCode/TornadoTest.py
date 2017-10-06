# -*- coding:utf-8 -*-
# Author: Jason Lee

import tornado.web
import tornado.ioloop

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('Hello world!')

if __name__ == '__main__':
    app = tornado.web.Application([(r'/', IndexHandler)])
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
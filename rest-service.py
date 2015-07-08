#!/bin/env python
# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write({"status": 200, "condition": 1})

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8080)
    tornado.ioloop.IOLoop.instance().start()


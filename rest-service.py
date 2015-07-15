#!/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

import inspection_cls

from tornado.options import define, options

define('port', default=8080, help="port to listen on")

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", HomeHandler),
            (r"/diagnose", DiagnoseHandler),
        ]
        settings = dict(
            debug=True,
        )
        super(Application, self).__init__(handlers, **settings)

class BaseHandler(tornado.web.RequestHandler):
    @property
    def get_current_user(self):
        return None

class HomeHandler(BaseHandler):
    def get(self):
        self.write({"status": 200, "message": "It works!!"})

class DiagnoseHandler(BaseHandler):
    def get(self):
        # TODO API-CALL
        # export PYTHONPATH=/opt/t4j/chainerapp(~/.bashrc)
        ins = inspection_cls.Inspection()
        ret = ins.execute('/var/opt/t4j/chainer-data/tmpimages/image0000000.jpg')
        self.write({"status": 200, "condition": ret[0,0], "score": ret[0,1]})


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()

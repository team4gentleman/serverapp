#!/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

import os, uuid
from PIL import Image, ImageFilter

import inspection_cls

__UPLOADS__ = "/var/opt/t4j/chainer-data/tmpimages/"

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
    def post(self):
        fileinfo = self.request.files['filearg'][0]
        print ("fileinfo is"), fileinfo
        fname = fileinfo['filename']
        extn = os.path.splitext(fname)[1]
        cname = str(uuid.uuid4()) + extn
        fh = open(__UPLOADS__ + cname, 'wb')
        print (fileinfo['body'])
        fh.write(fileinfo['body'])

        # API-CALL
        ins = inspection_cls.Inspection()
        ret = ins.execute(__UPLOADS__ + cname)

        # TODO
        self.write({"status": 200, "diagnoses": [{"runk": 1, "condition": ret[0,0], "score": ret[0,1]},{"runk": 1, "condition": ret[1,0], "score": ret[2,1]}]})


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()

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

import numpy as np

__UPLOADS__ = "/var/opt/t4j/chainer-data/tmpimages/"

from tornado.options import define, options

define('port', default=8080, help="port to listen on")

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", HomeHandler),
            (r"/form", UserformHandler),
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

class UserformHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("fileuploadform.html")

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
        ret = np.array(ret)

        # ins.executeからの返り値の想定
        #ret = np.array([
        #           ('female', 0.20466148853302002),
        #           ('50', 0.1924593597650528),
        #           ('male', 0.07535989582538605),
        #           ('40', 0.07535989582538605),
        #           ('drunker', 0.07535989582538605),
        #           ('bad', 0.07535989582538605),
        #           ('good', 0.07535989582538605),
        #           ('drunker', 0.07535989582538605),
        #           ('drunker', 0.07535989582538605)
        #        ])
        
        ################# メッセージの評価 #################

        # カテゴリは以下の前提
        sex_a = np.array(['male', 'female'])
        age_a = np.array(['50', '40', '30'])
        health_a = np.array(['good', 'bad', 'drunker'])
        
        sex = ""
        age = ""
        health = ""
        
        for var in reversed(range(1, ret.shape[0]+1)):
         condition = str(ret[var-1,0])
         for var in range(0, sex_a.size):
          if condition == sex_a[var]:
           sex = sex_a[var]
         for var in range(0, age_a.size):
          if condition == age_a[var]:
           age = age_a[var]
         for var in range(0, health_a.size):
          if condition == health_a[var]:
           health = health_a[var]
        
        #print(sex)
        #print(age)
        #print(health)
        
        message = ""
        
        # 要メッセージ調整
        if (sex == 'male') and (age == '50') and (health == 'good'):      message = "男性、50歳、調子よさそうですね！"
        if (sex == 'male') and (age == '50') and (health == 'bad'):       message = "男性、50歳、疲れていますね！"
        if (sex == 'male') and (age == '50') and (health == 'drunker'):   message = "男性、50歳、酔っ払っていますね！"
        if (sex == 'male') and (age == '40') and (health == 'good'):      message = "男性、40歳、調子よさそうですね！"
        if (sex == 'male') and (age == '40') and (health == 'bad'):       message = "男性、40歳、疲れていますね！"
        if (sex == 'male') and (age == '40') and (health == 'drunker'):   message = "男性、40歳、酔っ払っていますね！"
        if (sex == 'male') and (age == '30') and (health == 'good'):      message = "男性、30歳、調子よさそうですね！"
        if (sex == 'male') and (age == '30') and (health == 'bad'):       message = "男性、30歳、疲れていますね！"
        if (sex == 'male') and (age == '30') and (health == 'drunker'):   message = "男性、30歳、酔っ払っていますね！"
        if (sex == 'female') and (age == '50') and (health == 'good'):    message = "女性、50歳、お肌の調子よさそうですね！"
        if (sex == 'female') and (age == '50') and (health == 'bad'):     message = "女性、50歳、お疲れですか？"
        if (sex == 'female') and (age == '50') and (health == 'drunker'): message = "女性、50歳、酔っちゃいました？"
        if (sex == 'female') and (age == '40') and (health == 'good'):    message = "女性、40歳、お肌の調子よさそうですね！"
        if (sex == 'female') and (age == '40') and (health == 'bad'):     message = "女性、40歳、お疲れですか？"
        if (sex == 'female') and (age == '40') and (health == 'drunker'): message = "女性、40歳、酔っちゃいました？"
        if (sex == 'female') and (age == '30') and (health == 'good'):    message = "女性、30歳、お肌の調子よさそうですね！"
        if (sex == 'female') and (age == '30') and (health == 'bad'):     message = "女性、30歳、お疲れですか？"
        if (sex == 'female') and (age == '30') and (health == 'drunker'): message = "女性、30歳、酔っちゃいました？"
        
        # print(message)
        
        ################# jsonレスポンスの組み立て #################
        
        res1 = "{\"status\": 200, \"message\": \"" + message + "\", \"diagnoses\": ["
        
        res2 = ""
        
        for var in range(1, ret.shape[0]+1):
         rank = str(var)
         condition = str(ret[var-1,0])
         score = str(ret[var-1,1])
         res2 += "{\"rank\": " + rank + ", \"condition\": \"" + condition + "\", \"score\": " + score + "},"
        
        # 最後の,を除去
        res2 = res2[:-1]
        
        res3="]}"
        
        resall = res1 + res2 + res3

        self.write(resall)

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()

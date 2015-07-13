import tornado
import tornado.ioloop
import tornado.web
import os, uuid
from PIL import Image, ImageFilter

__UPLOADS__ = "uploads/"

# フォームから画像をアップするサンプル
 
class Userform(tornado.web.RequestHandler):
    def get(self):
        self.render("fileuploadform.html")
 
class Upload(tornado.web.RequestHandler):
    def post(self):
        fileinfo = self.request.files['filearg'][0]
        print ("fileinfo is"), fileinfo
        fname = fileinfo['filename']
        extn = os.path.splitext(fname)[1]
        cname = str(uuid.uuid4()) + extn
        fh = open(__UPLOADS__ + cname, 'wb')
        print (fileinfo['body'])
        fh.write(fileinfo['body'])
        self.finish(cname + " is uploaded!! Check %s folder" %__UPLOADS__)
 

# RESTできた画像を受け取って、chainappに流して、結果を流すサンプル（作成中）

class MobileNurseRest(tornado.web.RequestHandler):
    def post(self):
        # デバッグ用
        print (self.request)
        print (self.request.protocol)
        print (self.request.body)

        # RESTのUPLOADの仕方によるか？
        # 現状の下記のwgetサンプルの呼び方だとファイルハンドラに区切り用ヘッダが入ってしまう★
        # curl -X POST -F fileUpload=@mn_logo_b.jpg http://localhost:8888/mobilenurserest
        cname = str(uuid.uuid4()) + ".jpg"
        fh = open(__UPLOADS__ + cname, 'wb')
        fh.write(self.request.body)
        
        # chainerappを呼んで結果をもらう★
        # ・・・
        # ・・・
        
        # 結果に従い、ファイルを加工し、それをバイナリで返す。★
        # cname_2 = str(uuid.uuid4()) + ".jpg"
        # fh_2 = open(__UPLOADS__ + cname, 'wb')
        # fh_2.write(self.request.body)
        # self.finish(cname + " is uploaded!! Check %s folder" %__UPLOADS__)
        
        # 画像編集ライブラリテスト用★
        original = Image.open(__UPLOADS__ + "59b6c1c9-1fd4-4664-89a7-9905c88b6e39.jpg") # ハードドライブから画像をロード
        blurred = original.filter(ImageFilter.BLUR) # 画像をぼかす
        original.show() # 2つの画像を表示する
        blurred.show()

application = tornado.web.Application([
        (r"/", Userform),
        (r"/upload", Upload),
        (r"/mobilenurserest", MobileNurseRest),
        ], debug=True)
 
 
if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
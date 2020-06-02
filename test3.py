#encoding=utf-8
import tornado.web
import tornado.ioloop
import os

class UploadHandler(tornado.web.RequestHandler):
    def get(self,*args,**kwargs):
        self.render('templates/upload.html')

    def post(self,*args,**kwargs):
        img1 = self.request.files['img']
        for img in img1:
            body=img.get('body','')
            content_type=img.get('content_type','')
            filename=img.get('filename','')

        dir=os.path.join(os.getcwd(),'file',filename)
        with open(dir,'wb') as fw:
            fw.write(body)

        self.set_header('Content-Type',content_type)
        self.write(body)


app = tornado.web.Application([
    (r'/upload/',UploadHandler),
])

app.listen(8888)

tornado.ioloop.IOLoop.instance().start()
#encoding=utf-8
import tornado.web
import tornado.ioloop
from tornado.escape import json_encode


class IndexHandler(tornado.web.RequestHandler):
    def get(self,*args,**kwargs):
        self.render('templates\login.html')


class LoginHandler(tornado.web.RequestHandler):
    def get(self,*args,**kwargs):
        name=self.get_argument('name')
        pwd=self.get_argument('pwd')
        user=[name,pwd]
        self.write(json_encode(user))

    def post(self,*args,**kwargs):
        name=self.get_body_argument('name')
        pwd=self.get_body_argument('pwd')
        user=[name,pwd]
        self.write(json_encode(user))

app = tornado.web.Application([
    (r'^/$',IndexHandler),
    (r'^/login/$',LoginHandler),
])

app.listen(8888)

tornado.ioloop.IOLoop.instance().start()
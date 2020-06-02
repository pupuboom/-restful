import tornado.web
import tornado.ioloop

class IndexHandler(tornado.web.RequestHandler):
    def get(self,*args,**kwargs):
        self.write("Hello World!")

app = tornado.web.Application([
    (r'/',IndexHandler)
])

app.listen(8888)

tornado.ioloop.IOLoop.instance().start()
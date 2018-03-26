import tornado.web
import tornado.ioloop


class IndexHandler(tornado.web.RequestHandler):
    '''主路由处理类'''
    def get(self):
        '''对应http的get请求'''
        self.write('hello world')

if __name__ == '__main__':
    app = tornado.web.Application([
        (r'/', IndexHandler),
    ])
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()

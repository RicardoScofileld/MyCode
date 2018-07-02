import tornado.web
import tornado.ioloop


class MainHandler(tornado.web.RequestHandler):
    '''主路由处理类'''
    def get(self):
        '''对应http的get请求'''
        self.write('You Requested the main page!!!')


class StoryHandle(tornado.web.RequestHandler):
    
    def get(self, story_id):
        self.write("You Requested the story" + story_id)



if __name__ == '__main__':
    app = tornado.web.Application([
        (r'/', MainHandler),
        (r'/story/([0-9]+)', StoryHandle),
    ])
    app.listen(8000)
    # 开启多线程,bind端口，start里面指定开启的进程数量，默认为1，如果为None或者为0，则自动根据机器的cpu生成对应的线程数量，如果大于0，则创建该数量的线程
    # http_server = tornado.httpserver.HTTPServer(app)
    # http_server.bind(8000)
    # http_server.start(0)
    tornado.ioloop.IOLoop.current().start()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/5 下午6:29
# @Author  : renzhiwen
# @Email   : zhiwen.ren@apicloud.com
# @File    : test_tornado.py
# @Description : 测试

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options


define('port', default=8000, help="run on the given port", type=int)


class IndexHandle(tornado.web.RequestHandler):

    def get(self):
        greeting = self.get_argument("greeting", "hello")
        self.write(greeting + ', friendly user')


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[
        (r'/', IndexHandle)
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
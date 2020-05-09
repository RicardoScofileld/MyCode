#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/5 下午6:46
# @Author  : renzhiwen
# @Email   : zhiwen.ren@apicloud.com
# @File    : string_service.py
# @Description :

import textwrap
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options


define("port", default=8000, help="run on the given port", type=int)


class ReverseHandle(tornado.web.RequestHandler):

    def get(self, input):
        self.write(input[::-1])


class WrapHandle(tornado.web.RequestHandler):

    def post(self):
        text = self.get_argument('text')
        width = self.get_argument('width', 40)
        self.write(textwrap.fill(text, int(width)))


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[
        (r'/reverse/(\w+)', ReverseHandle),
        (r'/wrap', WrapHandle)
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
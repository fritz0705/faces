#!/usr/bin/env python3
# coding: utf-8

import clintonfaces
import bottle
import pymongo
import tornado.web, tornado.wsgi, tornado.httpserver, tornado.ioloop, tornado.netutil

clintonfaces.db = pymongo.Connection().clintonfaces
app = tornado.web.Application([
	(r"/.*", tornado.web.FallbackHandler, dict(fallback=tornado.wsgi.WSGIContainer(clintonfaces.app)))
])

socks = [ tornado.netutil.bind_unix_socket("clintonfaces.sock", mode=0o666) ]
server = tornado.httpserver.HTTPServer(app)
server.add_sockets(socks)

tornado.ioloop.IOLoop.instance().start()

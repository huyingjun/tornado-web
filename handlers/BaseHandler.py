#coding:utf-8
from tornado.web import RequestHandler

class BaseHandler(RequestHandler):
    @property
    def db(self):
        return self.Application.db
    @property
    def redis(self):
        return self.Application.redis

    def initialize(self):
        pass

    def prepare(self):
        pass

    def write_error(self, status_code, **kwargs):
        pass

    def set_default_headers(self):
        pass

    def on_finish(self):
        pass


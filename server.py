#coding:utf-8
import torndb
import redis
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
import tornado.log
from tornado.options import define,options
from urls import handler
from config import setting,mysql_options,redis_options,logs_config
define('port',type=int,default=8000,help="端口")

class Application(tornado.web.Application):
    def __init__(self):
        super(Application, self).__init__()
        self.db = torndb.connection(mysql_options)
        self.redis = redis.StrictRedis(redis_options)

def main():
    options.log_file_prefix=logs_config["logs_file"]
    options.log_rotate_mode=logs_config["logs_mode"]
    options.log_rotate_when=logs_config["logs_when"]
    options.logging=logs_config["logs_level"]
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handler,**setting
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()

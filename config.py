#coding: utf-8
import os
from tornado.log import LogFormatter
#application 配置
setting = {
    "static_path":os.path.join(os.path.dirname(__file__),"static"),
    "template_path":os.path.join(os.path.dirname(__file__),"template"),
    "cookie_secret": "oDypkDrhT5uLpTraiecelVOj7gUgREGRjgx+4FFTa3k=",
    "xsrf_cookies": False,
    "login_url": "/login",
    "debug":True,
}

#mysql 配置
mysql_options = {
    "host" : "localhost",
    "database" : "ihome",
    "user" : "root",
    "password" : "h1y2j3"
}

#redis 配置
redis_options = {
    "host" : "localhost",
    "port" : 6379
}

# logging 日志
logs_config = {
    "logs_file" : os.path.join(os.path.dirname(__file__),"logs/log"),
    "logs_level" : "info",
    "logs_mode" : "time",
    "logs_when" : "D"
}
#coding: utf-8
import logging
import tornado.log
from .BaseHandler import BaseHandler

class IndexHandler(BaseHandler):
    def get(self):
        logging.debug('debug ...')
        logging.info('info ...')
        logging.warning('warning ...')
        logging.error('error ...')
        self.write('hello word')
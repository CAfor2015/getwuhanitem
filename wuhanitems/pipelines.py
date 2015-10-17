# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from twisted.enterprise import adbapi
import time
import MySQLdb
import MySQLdb.cursors
import logging

class WuhanitemsPipeline(object):

  def __init__(self):
    self._dbpool = adbapi.ConnectionPool(
      'MySQLdb',
      db = 'scrapyuse',
      user = 'adminpy',
      passwd = 'abc123',
      cursorclass = MySQLdb.cursors.DictCursor,
      charset = 'utf8',
      use_unicode = True)
   
  def process_item(self, item, spider):
    query = self._dbpool.runInteraction(self._conditional_insert, item)
    query.addErrback(self.handle_error)
    return item

  def _conditional_insert(self, tx, item):
    if item:
      tx.execute(\
        "insert into shopinfo_shopinformation (name, addr, tel) \
        values(%s, %s, %s)", 
        (item["name"], 
         item["addr"], 
         item["tel"]))
      tx.execute("commit")

  def handle_error(self, e):
    logging.error(e)

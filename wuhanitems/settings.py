# -*- coding: utf-8 -*-

# Scrapy settings for wuhanitems project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

#BOT_NAME = 'wuhanitems'

SPIDER_MODULES = ['wuhanitems.spiders']
NEWSPIDER_MODULE = 'wuhanitems.spiders'
#DOWNLOAD_HANDLERS = {'s3': None}
#COOKIES_DEBUG = True
#COOKIES_ENABLED = False

DOWNLOAD_DELAY=0.25

ITEM_PIPELINES = ['wuhanitems.pipelines.WuhanitemsPipeline',]

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36',


HEADER = {
  "Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
  "Accept-Encoding:gzip, deflate, sdch",
  "Accept-Language:zh-CN,zh;q=0.8",
  "Cache-Control:max-age=0",
  "Connection:keep-alive",
  "Host:www.dianping.com",
  "User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36",
}


#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scrapy
from wuhanitems.items import WuhanitemsItem

class WhSpider(scrapy.Spider):
  name = 'whspider'
  allowed_domain = ['dianping.com']
  start_urls = [
    'http://www.dianping.com/search/category/16/45/g147'
    ]

  def parse(self, response):
    _root_url = 'http://www.dianping.com'
    # parse url for shop home page
    _hxs = scrapy.Selector(response)
    _link = _hxs.xpath(
      '//div[@class="shop-wrap"]//div[@class="tit"]/a[@data-hippo-type="shop"]/@href').extract()
    for url in _link:
      print 'URL is:', url
      if url:
        _shop_url = _root_url + url
        yield scrapy.Request(_shop_url, callback=self.parse_info)

    # parse next page url info 
    _link_page = _hxs.xpath('//div[@class="page"]/a[@class="next"]/@href').extract()
    if len(_link_page):
      _url = _link_page[0]
      _next_page = _root_url + _url
      yield scrapy.Request(_next_page, callback=self.parse)
  
  def parse_info(self, response):
    # parse info in shop home page
    item = WuhanitemsItem()
    hxs = scrapy.Selector(response)
    item['name'] = hxs.xpath("//div[@class='breadcrumb']/span/text()").extract()[0].encode('utf-8')
    item['tel'] = ' '.join(hxs.xpath("//span[@itemprop='tel']/text()").extract()).encode('utf-8')
    item['addr'] = hxs.xpath("//span[@itemprop='street-address']/@title").extract()[0].encode('utf-8')
    yield item

 

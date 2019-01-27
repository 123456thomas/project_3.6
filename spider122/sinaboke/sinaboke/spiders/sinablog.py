# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import SinabokeItem

class SinablogSpider(CrawlSpider):
    name = 'sinablog'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://sina.com.cn/']

    pagelink = LinkExtractor()
    contentlink = LinkExtractor()

    def parse(self, response):
        pass

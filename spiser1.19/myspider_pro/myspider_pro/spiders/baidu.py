# -*- coding: utf-8 -*-
"""
https://www.taobao.com/markets/tbhome/cool-shop?spm=a21bo.7929913.198967.9.20384174AU6t8q&categoryId=2102
https://www.taobao.com/markets/tbhome/cool-shop?spm=a21bo.7929913.198967.8.15d64174OgsJB5&categoryId=2101
"""

import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        print(response.text)

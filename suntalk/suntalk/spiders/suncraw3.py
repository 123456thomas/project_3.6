# -*- coding: utf-8 -*-
'''
@RedisCrawlSpider
分布式爬取
深度的爬取
'''

import scrapy
from scrapy_redis.spiders import RedisCrawlSpider
from scrapy.spider import Rule
from scrapy.linkextractors import LinkExtractor
from ..items import SuntalkItem

class Suncraw3Spider(RedisCrawlSpider):
    name = 'suncraw3'
    redis_key = "suncraw3:start_urls"

    # 翻页的链接提取器
    pagelink = LinkExtractor(restrict_xpaths=('//div[@class="pagination"]/a[text()=">"]'))
    # 帖子内容的链接提取器
    contentlink = LinkExtractor(restrict_xpaths=('//a[@class="news14"]'))
    # 构建规则
    rules = [
        Rule(pagelink,process_links="deal_link",follow=True),
        Rule(contentlink,callback='parse_item',follow=True)
    ]

    def __init__(self, *args, **kwargs):
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(Suncraw3Spider, self).__init__(*args, **kwargs)

    def deal_link(self,links):
        for link in links:
            print('link:',link.url)
        return links

    def parse_item(self, response):
        '''
        处理请求到的详情页面
        :param response:
        :return:
        '''
        print("+"*20)
        title  = response.xpath('//div[@class="wzy1"]/table[1]/tr/td[2]/span[1]/text()').extract()[0]
        self.log('title:'+title)
        number = response.xpath('//div[@class="wzy1"]/table[1]/tr/td[2]/span[2]/text()').extract()[0]
        self.log('number:'+number)
        self.log("="*60)
        item = SuntalkItem()
        item["title"] = title
        item["number"] = number
        yield item
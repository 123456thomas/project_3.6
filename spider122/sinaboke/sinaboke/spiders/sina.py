# -*- coding: utf-8 -*-
# 目的：理解CrawlSpider含义及其用法

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import SinabokeItem
"""
从第一篇博文开始爬取
"""

class SinaSpider(CrawlSpider):
    name = 'sina'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://blog.sina.com.cn/s/blog_5af303e30102y8ae.html']
    nums = 0

    # 网页的翻页提取
    next_page_link = LinkExtractor(restrict_xpaths=('//div[@class="articalfrontback SG_j_linedot1 clearfix"]/div[1]/a','//div[@class="clearfix pageBox"]/span[1]/a'))

    rules = [
        Rule(next_page_link, callback='parse_item', follow=True)
    ]

    def parse_item(self, response):
        '''
        处理请求到的详情页面
        :param response:
        :return:
        '''
        print("++"*20)
        title  = response.xpath('//div[@class="articalTitle"]/h2/text()').extract()
        if len(title) > 0:
            title = title[0]
        else:
            title = response.xpath('//div[@class="articalTitle"]/h1/text()').extract()
            if len(title) > 0:
                title = title[0]
            else:
                title = response.xpath('//div[@class="BNE_title"]/h1/text()').extract()
                if len(title) > 0:
                    title = title[0]
                else:
                    title = '空'
        url = response.url
        print('Boke_url:=====',url)
        print('Boke_title:=====',title)
        self.nums += 1
        item = SinabokeItem()
        item['title'] = title
        item['url'] = url
        print(self.nums)
        yield item
        # pub_date  = response.xpath('//span[@class="time SG_txtc"]/h2/text()').extract()[0]
        # print('title:',title)
        # read_num = response.xpath('//div[@class="articalInfo"]/div[@class="IL"]/span[1]/text()').extract()[0]
        # imgs = response.xpath('//*[@id="sina_keyword_ad_area2"]/p/img').extract()
        # imgs = ";".join(imgs)
        # print('pub_date:',pub_date)
        # print('read_num:',read_num)
        # print('number:',imgs)
        # print('imgs:',imgs)
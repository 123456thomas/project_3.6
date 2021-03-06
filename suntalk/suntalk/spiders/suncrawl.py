# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import SuntalkItem

class SuncrawlSpider(CrawlSpider):
    name = 'suncrawl'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4']
    # 1.创建提取器
    # 翻页的链接提取器
    pagelink = LinkExtractor(restrict_xpaths=('//div[@class="pagination"]/a[text()=">"]'))
    # 帖子内容的链接提取器
    contentlink = LinkExtractor(restrict_xpaths=('//a[@class="news14"]'))
    # 2.创建规则
    rules = [
        Rule(pagelink, process_links="deal_link", follow=True),
        Rule(contentlink, callback='parse_item')
    ]

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
        title  = response.xpath('//div[@class="wzy1"]/table[1]/tr/td[2]/span[1]/text()').extract()[0]
        self.log('title:'+title)
        number = response.xpath('//div[@class="wzy1"]/table[1]/tr/td[2]/span[2]/text()').extract()[0]
        self.log('number:'+number)
        self.log("="*60)
        item = SuntalkItem()
        item["title"] = title
        item["number"] = number
        yield item

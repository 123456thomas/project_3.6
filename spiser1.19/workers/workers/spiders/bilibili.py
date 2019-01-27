# -*- coding: utf-8 -*-
import scrapy
from ..items import WorkersItem


class BilibiliSpider(scrapy.Spider):
    name = 'bilibili'
    allowed_domains = ['bilibili.com']
    start_urls = ['https://www.bilibili.com/ranking#!/all/0/0/7/']

    def parse(self, response):
        contents = response.xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[3]/ul/li')
        print(len(contents))
        for content in contents:
            paihang = content.xpath('.//div[@class="num"]/text()').extract_first().strip()
            urls = content.xpath('.//div[@class="content"]/div[@class="info"]/a/@href').extract_first().strip()
            title = content.xpath('.//div[@class="content"]/div[@class="info"]/a/text()').extract_first().strip()
            socore = content.xpath('.//div[@class="content"]/div[@class="info"]/div[@class="pts"]/div/text()').extract_first().strip()
            print(paihang,urls,title,socore)
            print('='*60)

            # 数据封装
            item = WorkersItem()
            item['paihang'] = paihang
            item['urls'] = urls
            item['title'] = title
            item['socore'] = socore

            yield item

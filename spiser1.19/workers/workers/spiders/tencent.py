# -*- coding: utf-8 -*-
import scrapy
import pyttsx3
import re
import time
from ..items import TencentItem
engine = pyttsx3.init()

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    start_urls = ['http://hr.tencent.com/position.php?&start=0#a']
    def __init__(self):
        self.max_pages = 283

    def parse(self, response):
        contents = response.xpath('//table[@class="tablelist"]//tr')[1:-1]
        for content in contents:
            offer = content.xpath('.//a[@target="_blank"]/text()').extract_first()
            types = content.xpath('./td[2]/text()').extract_first()
            number = content.xpath('./td[3]/text()').extract_first()
            city = content.xpath('./td[4]/text()').extract_first()
            pub_date = content.xpath('./td[5]/text()').extract_first()
            # print(offer,types,number,city,pub_date)

            # 数据封装
            item = TencentItem()
            item['offer'] = offer
            item['types'] = types
            item['number'] = number
            item['city'] = city
            item['pub_date'] = pub_date
            yield item

        # "&start=10#a,start=0#a"
        print(response.url)
        p = ".*?&start=(\d+).*?"
        next_page = int(int(re.search(p,response.url).group(1))/10)+1
        print('下一页=====',next_page)
        if next_page < self.max_pages:
            next_url = "http://hr.tencent.com/position.php?&start=%s#a" % (10 * next_page)
            engine.say("第%s页采集完毕"%next_page)
            engine.runAndWait()
            yield response.follow(next_url,self.parse)
        else:
            print('数据读取完毕')
            engine.say("采集结束")
            engine.runAndWait()

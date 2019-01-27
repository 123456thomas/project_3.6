# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
from bs4 import BeautifulSoup
from ..items import TushuItem
import re

class OreillySpider(scrapy.Spider):
    name = 'oreilly'
    allowed_domains = ['oreilly.com.cn']
    start_urls = ['http://www.oreilly.com.cn/index.php?func=completelist']

    def parse(self, response):
        html = response.text
        soup = BeautifulSoup(html ,'html')
        print(soup.title)
        lis =(x for x in soup.select('div.completelist_book_brief > table > tbody > tr')[1:])
        print(lis)
        for li in lis:
            name = li.select('td')[0].get_text().strip()
            name = name.replace("，","_")
            pubtime = li.select('td')[1].get_text().strip()
            price = li.select('td')[2].get_text().strip()
            print(name,pubtime,price)

            partten = re.compile(r'(\d+)', re.I | re.S)
            result_pr = re.findall(partten, price)
            if len(result_pr) > 2:
                result_pr = ",".join(result_pr[:-1]) + "." + result_pr[-1]
            else:
                result_pr = ".".join(result_pr)
            result_time = re.findall(partten, pubtime)
            result_time = "-".join(result_time)
            item = TushuItem()
            item['name'] = name
            item['pubtime'] = result_time
            item['price'] = result_pr
            yield item

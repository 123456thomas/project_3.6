# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import DouyuimgItem


class CapidouyuSpider(scrapy.Spider):
    name = 'capidouyu'
    allowed_domains = ['capi.douyucdn.cn']
    url = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset='
    offset = 0
    start_urls = [url + str(offset)]

    def parse(self, response):
        # 返回从 json 里获取 data 段数据集合
        data = json.loads(response.text)["data"]

        for each in data:
            item = DouyuimgItem()
            item["name"] = each["nickname"]
            item["imagesUrls"] = each["vertical_src"]
            item["imagesPath"] = each["vertical_src"]
            yield item

        self.offset += 20
        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)


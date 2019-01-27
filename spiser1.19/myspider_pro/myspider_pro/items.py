# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderProItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class JobItem(scrapy.Item):
    """工作数据类型"""
    name = scrapy.Field()
    corpt = scrapy.Field()
    city = scrapy.Field()
    salary = scrapy.Field()
    pub_date = scrapy.Field()

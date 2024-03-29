# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WorkersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    paihang = scrapy.Field()
    urls = scrapy.Field()
    title = scrapy.Field()
    socore = scrapy.Field()

class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    offer = scrapy.Field()
    types = scrapy.Field()
    number = scrapy.Field()
    city = scrapy.Field()
    pub_date = scrapy.Field()

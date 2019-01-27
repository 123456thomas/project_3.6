# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class DoubanmoveItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    daoyan = scrapy.Field()
    bianju = scrapy.Field()
    jianjie = scrapy.Field()
    sorts = scrapy.Field()
    actor = scrapy.Field()
    score = scrapy.Field()
    talknum = scrapy.Field()


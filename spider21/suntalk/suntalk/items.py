# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SuntalkItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    identifier = scrapy.Field()
    sun_url = scrapy.Field()
    sun_title = scrapy.Field()
    sun_author = scrapy.Field()
    pub_date = scrapy.Field()
    sun_cont = scrapy.Field()

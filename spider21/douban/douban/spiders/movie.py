# -*- coding: utf-8 -*-
"""
豆瓣电影 top 250 爬虫， 电影的名称，简介，评分，引文，存储到 mangodb 数据库
https://movie.douban.com/top250?start=0&filter=
"""
import scrapy


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['douban.com']
    start_urls = ['http://douban.com/']

    def parse(self, response):
        pass

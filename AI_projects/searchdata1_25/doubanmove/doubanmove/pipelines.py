# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import codecs

class DoubanmovePipeline(object):
    def __init__(self):
        self.file = codecs.open('douyu.csv', 'a',encoding='utf8')
        self.wr = csv.writer(self.file, dialect='excel')
        self.wr.writerow(['title', 'daoyan', 'bianju', 'sorts', 'actor', 'score', 'talknum', 'jianjie'])

    def process_item(self, item, spider):
        self.wr.writerow([item["title"],item['daoyan'],item["bianju"],item["sorts"],item["actor"],item["score"],item["talknum"],item["jianjie"]])
        return item

    def close_item(self,spider):
        self.file.close()
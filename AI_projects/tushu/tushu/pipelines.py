# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import csv

class TushuPipeline(object):
    def __init__(self):
        self.file = codecs.open('oreilly.csv', 'a',encoding='utf8')
        self.wr = csv.writer(self.file, dialect='excel')
        self.wr.writerow(['name', 'pubtime', 'price'])

    def process_item(self, item, spider):
        self.wr.writerow([item["name"],item['pubtime'],item["price"]])
        return item

    def close_item(self,spider):
        self.file.close()

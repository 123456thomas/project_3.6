# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import csv
import codecs


class JobspiderPipeline(object):
    def __init__(self):
        self.file = codecs.open('51job.csv','w','utf8')
        self.wr = csv.writer(self.file, dialect='excel')
        self.wr.writerow(['name', 'pub_date', 'city', 'corpt', 'salary'])

    # 当有数据提交过来，该函数会被触发
    def process_item(self, item, spider):
        self.wr.writerow(['name', 'pub_date', 'city', 'corpt', 'salary'])
        return item

    def close_spider(self, spider):
        self.file.close()

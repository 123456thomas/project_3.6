# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import codecs
import pymysql


# class WorkersPipeline(object):
#
#     def __init__(self):
#         self.file = codecs.open('bilibili.csv', 'w', 'utf8')
#         self.wr = csv.writer(self.file, dialect='excel')
#         self.wr.writerow(['paihang', 'urls', 'title', 'corpt', 'socore'])
#
#     def process_item(self, item, spider):
#         self.wr.writerow([item["paihang"],item['urls'],item["title"],item["socore"]])
#         return item
#
#     def close_item(self,spider):
#         self.file.close()

class WorkersPipeline(object):
    def process_item(self, item, spider):
        """爬虫程序每yield一个item,就执行一次"""
        sql = "insert into tencentjobs(offer,types,number,city,pub_date) value(%s,%s,%s,%s,%s)"
        self.cursor.execute(sql,(item['offer'],item['types'],item['number'],item['city'],item['pub_date']))
        self.conn.commit()
        return item

    def open_spider(self, spider):
        """
        爬虫程序启动时执行，并且只执行一次.
            链接数据库，获取sql的cursor，打开文件，连接网络
        """

        self.conn = pymysql.connect(host="", user="root", password="361365",
                 database="scrapy_pro", port=3306,charset='utf8')
        self.cursor = self.conn.cursor()
        pass

    def close_spider(self, spider):
        """爬虫程序启动时执行，并且只执行一次
        链接数据库，获取sql的cursor，关闭文件，关闭网络连接
        """
        self.conn.commit()  # 最后再提交一次,确保数据的完整性
        self.cursor.close()
        self.conn.close()

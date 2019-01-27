# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
# 可以创建多个管道类，但要添加到配置中
class MyspiderProPipeline(object):
    def process_item(self, item, spider):
        """爬虫程序每yield一个item,就执行一次"""
        print(item['name'])
        sql = "insert into tencentjobs(name,company,salary,city,pub_time) value(%s,%s,%s,%s,%s)"
        self.cursor.execute(sql,(item['name'],item['corpt'],item['salary'],item['salary'],item['pub_date']))
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


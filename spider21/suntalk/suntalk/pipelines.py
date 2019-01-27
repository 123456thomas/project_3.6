# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql


class SuntalkPipeline(object):
    def open_spider(self,spider):
        self.con = pymysql.connect(host="", user="root", password="361365",
                                    database="scrapy_pro", port=3306, charset='utf8')
        self.cursor = self.con.cursor()

    def process_item(self, item, spider):
        """爬虫程序每yield一个item,就执行一次"""
        sql = "insert into suntalk(identifier,sun_url,sun_title,sun_author,pub_date,sun_cont) value(%s,%s,%s,%s,%s,%s)"
        self.cursor.execute(sql, (item['identifier'], item['sun_url'], item['sun_title'], item['sun_author'], item['pub_date'], item['sun_cont']))
        self.con.commit()
        return item

    def close_spider(self, spider):
        """爬虫程序启动时执行，并且只执行一次
        链接数据库，获取sql的cursor，关闭文件，关闭网络连接
        """
        self.con.commit()  # 最后再提交一次,确保数据的完整性
        self.cursor.close()
        self.con.close()
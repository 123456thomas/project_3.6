# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.conf import settings


class DouyuimgPipeline(ImagesPipeline):
    IMAGES_STORE = settings.get('IMAGES_STORE')

    def get_media_requests(self, item, info):
        imageUrl = item['imagesUrls']
        yield scrapy.Request(imageUrl)

    def item_completed(self, results, item, info):
        print("self.IMAGES_STORE:",self.IMAGES_STORE)
        print("results:", results)
        print("item:", item)
        print("info:", info)

    # def process_item(self, item, spider):
    #     return item

"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/9/25'
# 淘宝每日好店，男人帮，女神之店，店铺信息爬取
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""

from scrapy import Spider

class XinlangSpider(Spider):
    # 爬虫的名字
    name = "taobao"
    # 定义域名限制
    allowed_domains = ["taobao.com.cn"]

    # 定义起始采集地址
    start_urls = ["https://www.taobao.com/markets/tbhome/cool-shop"
                ]

    def parse(self, response):
        lis = response.xpath("//div[@id='cool-shop-tabs']/div[@class='section']/ul/li/a/@href").extract()

        # print(response.body)
        print(lis)
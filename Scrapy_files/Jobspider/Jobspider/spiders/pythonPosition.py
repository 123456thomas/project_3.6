# -*- coding: utf-8 -*-
import scrapy
from ..items import JobspiderItem

class PythonpositionSpider(scrapy.Spider):
    name = 'pythonPosition'  # 爬虫的名字
    allowed_domains = ['51job.com']  # 域名列表
    start_urls = ["https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="]
    def parse(self, response):
        # print(response.body)
        jobs_ls = response.xpath("//div[@id='resultList']/div[@class='el']")
        print(jobs_ls)
        # jobs_ls.pop(0)
        print('jobs_ls len:', len(jobs_ls))
        for each in jobs_ls:
            name = each.xpath(".//p[@class='t1 ']//a/text()").extract()[0].strip()
            print('name:', name)
            corpt = each.xpath(".//span[@class='t2']/a/text()").extract()[0]
            print('corpt:', corpt)
            city = each.xpath(".//span[@class='t3']/text()").extract()[0]
            print('city:', city)
            salary = each.xpath(".//span[@class='t4']/text()")
            if len(salary) > 0:
                salary = salary[0].extract()
            else:
                salary = ''
            print('salary:', salary)
            pub_date = each.xpath(".//span[@class='t5']/text()").extract()[0]
            print('pub_date:', pub_date)
            print('=' * 60)

            item =JobspiderItem()
            item['name'] = name
            item['corpt'] = corpt
            item['city'] = city
            item['salary'] = salary
            item['pub_date'] = pub_date

            # 将获取的数据交给pipelines
            yield item
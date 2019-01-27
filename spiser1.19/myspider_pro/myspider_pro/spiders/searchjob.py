"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/9/25'
# code is far away from bugs with the god animal protecting
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
from ..items import JobItem

class SearchJob(Spider):
    # 爬虫名称
    name = 'searchjob'
    allowed_domains = ['51job.com']
    start_urls = ['https://search.51job.com/list/020000,000000,0000,00,9,99,Python%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=']

    def parse(self, response):
        # 采集当前页面所有工作
        jobs_ls = response.xpath("//div[@id='resultList']/div[@class='el']")
        print(jobs_ls)
        # jobs_ls.pop(0)
        print('jobs_ls len:', len(jobs_ls))
        for each in jobs_ls:
            name = each.xpath(".//p[@class='t1 ']//a/text()")
            if len(name) > 0:
                name = name[0].extract()
            else:
                name = ''
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

            item = JobItem()
            item['name'] = name
            item['corpt'] = corpt
            item['city'] = city
            item['salary'] = salary
            item['pub_date'] = pub_date

            yield item

        next_page = response.xpath('//*[@id="resultList"]/div[55]/div/div/div/ul/li/a/@href').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
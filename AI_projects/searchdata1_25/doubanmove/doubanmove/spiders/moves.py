# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import DoubanmoveItem


class MovesSpider(CrawlSpider):
    name = 'moves'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250?start=0&filter=']
    # 1.构造 提取页面链接的 提取器
    next_link = LinkExtractor(restrict_xpaths=('//div[@class="paginator"]/span[@class="next"]/a'))
    content_link = LinkExtractor(restrict_xpaths=('//ol[@class="grid_view"]/li//div[@class="info"]/div[@class="hd"]/a'))
    # 2.构造规则
    rules = [
        Rule(next_link, callback="parse_item", follow=True),
        # Rule(content_link, callback="parse_item2")
    ]

    def parse_item(self, response):
        '''
        处理请求到的详情页面
        :param response:
        :return:
        '''
        lis_ = response.xpath('//ol[@class="grid_view"]/li')
        print("^ ^"*20)
        for lis in lis_:
            title = lis.xpath('.//div[@class="info"]/div[@class="hd"]/a/span/text()').extract()
            title = "|".join(title).replace("/", "|").strip()
            score = lis.xpath('.//div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()
            if len(score)>0:
                score = score[0].strip()
            else:
                print('空3')
                score = ''
            talknum = lis.xpath('.//div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[last()]/text()').extract()
            cont_link = lis.xpath('.//div[@class="info"]/div[@class="hd"]/a/@href').extract()[0]
            if len(talknum)>0:
                talknum = re.search(r'\d+',talknum[0].strip()).group()
            else:
                print('空4')
                talknum = ''

            item = DoubanmoveItem()
            item['title'] = title
            item['score'] = score
            item['talknum'] = talknum
            meta ={'item':item}
            yield response.follow(cont_link, callback=self.parse_item2, meta=meta)

    def parse_item2(self,response):
        item = response.meta['item']
        daoyan = response.xpath('//div[@id="info"]/span[1]/span[@class="attrs"]/a/text()').extract()
        bianju = response.xpath('//div[@id="info"]/span[2]/span[@class="attrs"]/a/text()').extract()
        actor = response.xpath('//div[@id="info"]/span[3]/span[@class="attrs"]/a/text()').extract()
        sort1 = response.xpath('//div[@id="info"]/span[@property="v:genre"]/text()').extract()
        jianjie = response.xpath('//div[@id="link-report"]/span[@class="short"]/span[@property="v:summary"]/text()').extract()
        daoyan = "&".join(daoyan).strip()
        bianju = "&".join(bianju).strip()
        actor = "&".join(actor).strip()
        sorts = "&".join(sort1).strip()
        if len(jianjie)>0:
            jianjie = jianjie[0].strip()
        else:
            jianjie = ''
        # print("--1", daoyan)
        # print("--2", bianju)
        # print("--3", actor)
        # print("--4", jianjie)
        # print("--5", sorts,type(sorts))
        item['daoyan'] = daoyan
        item['bianju'] = bianju
        item['actor'] = actor
        item['jianjie'] = jianjie
        item['sorts'] = sorts
        print("--5" * 10)
        yield item



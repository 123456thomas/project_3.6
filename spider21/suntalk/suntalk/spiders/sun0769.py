# -*- coding: utf-8 -*-
import scrapy
from ..items import SuntalkItem


class Sun0769Spider(scrapy.Spider):
    name = 'sun0769'
    pages = 0
    allowed_domains = ['sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4']

    def parse(self, response):
        # print(response.body)   序列化：extract（）
        trs = response.xpath("//div[@id='morelist']/div/table[2]//table//tr")
        print(len(trs))
        for tr in trs:
            identifier = tr.xpath("./td[1]/text()").extract_first().strip()
            sun_url = tr.xpath("./td[2]/a[@class='news14']/@href").extract_first().strip()
            sun_title = tr.xpath("./td[2]/a[@class='news14']/text()").extract_first().strip()
            sun_author = tr.xpath("./td[4]/text()").extract_first().strip()
            pub_date = tr.xpath("./td[5]/text()").extract_first().strip()
            # print(identifier,sun_url,sun_title,sun_author,pub_date)

            item = SuntalkItem()
            item['identifier'] = identifier
            item['sun_url'] = sun_url
            item['sun_title'] = sun_title
            item['sun_author'] = sun_author
            item['pub_date'] = pub_date
            # yield item
            yield response.follow(sun_url,self.parse2,meta={'item': item})
            next_page = response.xpath("//*[@id='morelist']/div/div[3]/a[last()]/text()").extract_first()

        if next_page == ">>":
            self.pages += 1
            next_url = self.start_urls[0] +"&page=%s"%(self.pages*30)
            print(self.pages)
            print(">>")
            print(next_url)
            yield response.follow(next_url,self.parse)

    def parse2(self,response):
        # print(response.body)
        # cons = response.xpath("//div[@class='wzy1']/table[2]//tr[1]/td[@class='txt16_3']/text()").extract_first().strip()
        cons = response.xpath("//div[@class='wzy1']/table[2]//tr[1]/td[@class='txt16_3']//div[@class='contentext']/text()").extract()

        # print(cons, len(cons) == 0)
        if len(cons) == 0:
            cons = response.xpath("//div[@class='wzy1']/table[2]//tr[1]/td[@class='txt16_3']/text()").extract()
        cons = "".join(cons).strip()

        item = response.meta['item']
        item['sun_cont'] = cons

        yield item



__auto__ = "Manstein"
from scrapy import Spider
# 文字转语音模块
import pyttsx3
engine = pyttsx3.init()

class Myspider(Spider):
    """自定义爬虫程序，需要继承Spider类型，才能使用scrapy框架提供的爬虫功能"""
    # 爬虫的名字
    name = 'demon1'
    # 定义起始采集地址
    start_urls = ("http://quotes.toscrape.com/page/1/",)
    def parse(self, response):
        """解析返回的数据"""
        quotes = response.css("div.quote")
        for quote in quotes:
            yield {
                # 两个冒号表示获取里面的文本
                "text":quote.css("span.text::text").extract_first(),
                "author":quote.xpath("span/small[@class='author']/text()").extract_first()
            }

        # 提取下一页数据
        next_page = response.xpath("//li[@class='next']/a/@href").extract_first()
        engine.say("开始采集下一页")
        engine.runAndWait()
        if next_page:
            # 存在下一页,继续采集 -->请求交给scrapy,
            yield response.follow(next_page, self.parse)
        else:
            engine.say("数据采集完成传递")
            engine.runAndWait()















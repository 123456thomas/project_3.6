
import scrapy


class Goo(scrapy.Spider):

    def __init__(self, user_agent=''):
        self.user_agent = user_agent
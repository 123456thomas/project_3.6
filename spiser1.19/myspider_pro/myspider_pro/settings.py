# -*- coding: utf-8 -*-

# Scrapy settings for myspider_pro project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'myspider_pro'

SPIDER_MODULES = ['myspider_pro.spiders']
NEWSPIDER_MODULE = 'myspider_pro.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'myspider_pro (+http://www.yourdomain.com)'
# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
   'Cookie': "t=13df33ebaa4724e3032a8e2d88e25572; cna=22i7FCqtDRICAXug4dOS8sRT; miid=1134502075797207017; l=aBtHqXKxyYX5v_omoMajiXDgu707WP5PdqE31Mak-TEhN_G77RXy1Mro-VwW7_qC5sKy_K-5F; tracknick=%5Cu661F%5Cu706B%5Cu4E4B%5Cu6E9077; lgc=%5Cu661F%5Cu706B%5Cu4E4B%5Cu6E9077; tg=0; thw=cn; UM_distinctid=16865eacf89123-0ce399371ee19d-b781636-100200-16865eacf8ba7; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; v=0; cookie2=1d4278666c128d8dcb2d2db015e30b19; _tb_token_=eb3753e577f53; unb=2412877792; sg=726; _l_g_=Ug%3D%3D; skt=14d33480dbe10ec1; cookie1=Bqr7YLfLDWq04zkZjs%2Bc09Q6cZXLlXwQQ%2FtbL53fKWA%3D; csg=ef1f1f89; uc3=vt3=F8dByE%2Bjcv8K4HV6ffs%3D&id2=UUwRmDFw5qEQ5Q%3D%3D&nk2=s0%2BIdaIkd5pPxA%3D%3D&lg2=URm48syIIVrSKA%3D%3D; existShop=MTU0ODA3MzM0Mg%3D%3D; _cc_=W5iHLLyFfA%3D%3D; dnk=%5Cu661F%5Cu706B%5Cu4E4B%5Cu6E9077; _nk_=%5Cu661F%5Cu706B%5Cu4E4B%5Cu6E9077; cookie17=UUwRmDFw5qEQ5Q%3D%3D; mt=ci=2_1&np=; enc=M%2B6C9cE8FL3LZzbq1w7Uk9Ab05s2TPcm7Qh3qtvTmtKlwP3N25yYn37%2FK0Gv0lcOKEUAK70O550LG22p0RhQlA%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; _m_h5_tk=fd28c09828852fb83c6730694812d8ed_1548080563060; _m_h5_tk_enc=7e383ee93e02779a52216e5ced43c59e; uc1=cookie15=Vq8l%2BKCLz3%2F65A%3D%3D&cookie14=UoTYPmEvAu5Znw%3D%3D; isg=BCAgnhMpaCbvMtRRQAXYaeyZ8S4ygQjurui9YJox7DvOlcC_QjnUg_anKX2wJbzL",
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'myspider_pro.middlewares.MyspiderProSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'myspider_pro.middlewares.MyspiderProDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'myspider_pro.pipelines.MyspiderProPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

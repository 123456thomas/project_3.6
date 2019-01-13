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

"""level1:
1、中超新闻(re)爬虫
爬取新闻标题，url，keywords
http://sports.163.com/zc/
"""

import re, requests
import pymysql

def Web_get(urls):
    """
    获取页面的源码
    :param urls:
    :return:
    """
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
    response = requests.get(urls, headers=headers)
    html = response.text
    print(html)
    return html

def Spider_data(html):
    """
    抓取数据
    :param html:
    :return:
    """

def main():
    baseurl = "http://sports.163.com/zc/"
    # 翻页
    begins = int(input("起始页:"))
    ends = int(input("终止页页:"))
    nums = 0
    # 获取页面
    for i in range(begins, ends + 1):
        newurl = baseurl + str(i)
        html = Web_get(baseurl)



if __name__ == '__main__':
    main()


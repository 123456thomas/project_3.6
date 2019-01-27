"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/9/25'
# 爬取豆瓣电影信息
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

# 加载模块
import requests
import json



def craw1(index):
    """
    豆瓣电影的爬取
    :param index:
    :return:
    """
    baseurl = "https://movie.douban.com/tag/"
    header ="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0"
    response = requests.get(baseurl,headers=header)
    if response.status_code == 200:
        print(response.text)


if __name__ == '__main__':
    baseurl = "https://movie.douban.com/tag/#/"
    for i in range(3):
        craw1(i)
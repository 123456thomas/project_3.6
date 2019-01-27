"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/9/25'
# 1、爬取豆瓣电影
# https://movie.douban.com/j/new_search_subjects
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

"""
请求头：
sort: U
range: 0,10
tags: 魔幻
start: 0
countries: 美国
相应的json
casts: ["海莉·斯坦菲尔德", "小豪尔赫·兰登伯格", "约翰·塞纳", "杰森·德鲁克", "帕梅拉·阿德龙"]
cover: "https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2541662397.jpg"
cover_x: 1080
cover_y: 1590
directors: ["特拉维斯·奈特"]
id: "26394152"
rate: "7.2"
star: "35"
title: "大黄蜂"
url: "https://movie.douban.com/subject/26394152/"
"""


# 导入页面请求
import requests
import time, json
# 导入动态资源加载模块
from selenium import webdriver
# 导入智能等待模块
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def Ai_wait(wait, by_, position_, timeout=120):
    """
    只能等待设置，直到超时
    :param by_:
    :param position_:
    :param timeout:
    :return:
    """
    t1 = time.time()
    while True:
        try:
            elemkeyword = wait.until(EC.presence_of_element_located((deal, position)))
            t2 = time.time()
            return elemkeyword
            break
        except Exception as e:
            if t2 - t1 > timeout:
                print("请求超时")
                print(e)
                break
            pass



def web_get(url_, i):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
    # 1.构建webdriver实例获取页面
    param = {"sort": "U", "range": "0,10", "tags": "", "start": "%s"%(20*i), "countries": "美国", }
    response = requests.get(url_, headers=headers, params=param)
    while True:
        if response.status_code == 200:
            data = json.loads(response.text)["data"]
            if len(data)>0:
                print(len(data))
                for item in data:
                    casts = ",".join(item["casts"])
                    cover = item["cover"]
                    directors = ",".join(item["directors"])
                    rate = item["rate"]
                    star = item["star"]
                    title = item["title"]
                    url = item["url"]
                    print(casts, cover, directors, rate, star, title, url)
                return True
            else:
                # 数据爬取完毕
                return "a"
        else:
            time.sleep(5)
            print("响应中....")


def main():
    num1 = 0
    baseurl = "https://movie.douban.com/j/new_search_subjects"
    while True:
        stat = web_get(baseurl, num1)
        if stat == True:
            num1 += 1
            print(num1)
        elif stat == "a":
            break
        else:
            time.sleep(5)

if __name__ == '__main__':
    main()



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


import re, requests, time

# 导入数据库
import pymysql

# 导入多线程和队列
import threading
from multiprocessing import Manager




def Web_get(urls):
    """
    获取页面的源码
    :param urls:
    :return:
    """
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
    response = requests.get(urls, headers=headers)
    html = response.text
    # print(html)
    return html

def mysql_inset(name, *datalist):
    """
    在spider数据库中，创建表，并插入数据
    :param name:表名
    :param datalist:一条数据的列表形式
    :param ends:写入结束，关闭数据库
    :return:
    """
    # 1.构建连接对象
    con = pymysql.connect(host="localhost",
                          user="root",
                          password="361365",
                          database="spider",
                          port=3306)
    # 2.创建游标
    cur = con.cursor()

    # 3.开始交互,构建插入语句
    try:
        query2 ="insert into %s"%name
        query2 = query2 + " values(0,%s,%s,%s,%s,%s,%s)"
        cur.execute(query2, datalist)
        if con is not None:
            con.commit()
    except Exception as e:
        print(e)
    finally:
        cur.close()
        con.close()

def Spider_data(html, *args):
    """
    数据抓取
    :param html: 页面信息
    :param args: 正则匹配对象元组
    :return:
    """
    result1 = args[0].finditer(html)
    nums = 0
    for li in result1:
        temp = li.group()
        result2 = []
        for i in range(1,len(args)):
            temp2 = args[i].search(temp)
            Temp = temp2.group(1).strip()
            if len(Temp)>200:
                Temp = Temp[:200]
            result2.append(Temp)
        mysql_inset("news", *result2)

def main0(bgeins,ends):
    baseurl = "http://sports.163.com/special/00051C89/zc"
    # 构造匹配对象
    """<div class=news_item"""
    re_news = re.compile(r'<div class="news_item">.*?</div>.*?</div>.*?</div>', re.I|re.S)
    re_title = re.compile(r'<div class="news_item">.*?<h3>.*?<a .*?>(.*?)</a>', re.I | re.S)
    re_urls = re.compile(r'<div class="news_item">.*?<h3>.*?<a href="(.*?)"', re.I | re.S)
    re_key1 = re.compile(r'<div class="news_item">.*?<div class="keywords">.*?<a .*?>(.*?)</a>', re.I | re.S)
    re_key2 = re.compile(r'<div class="news_item">.*?<div class="keywords">.*?<a .*?</a>.*?<a .*?>(.*?)</a>', re.I | re.S)
    re_time = re.compile('<div class="news_item">.*?<div class="post_date">(.*?)</div>', re.I | re.S)
    re_flow = re.compile(r'<div class="news_item">.*?<div class="share_join">.*?<span class="icon">(.*?)</span>', re.I | re.S)
    args = (re_news, re_title, re_urls, re_key1, re_key2, re_time, re_flow)

    # 获取页面
    for t in range(bgeins,ends+1):
        if t != 1:
            newurl = baseurl + "_%s.html"%(str(t).zfill(2))
        else:
            newurl = baseurl + ".html"
        html = Web_get(newurl)
        # 正则匹配获取数据
        Spider_data(html, *args)

def main():
    # 翻页
    begins = int(input("起始页:"))
    ends = int(input("终止页页:"))
    # 多线程处理,一个线程5页
    for t in (begins,ends+1,5):
        #  每个线程处理5页
        ts = threading.Thread(target=main0, args=((t,t+4)),)
        ts.start()
        print("线程数：", len(threading.enumerate()))
        end_page = t+5
        # 控制线程数,最多为4
        while len(threading.enumerate())>3:
            time.sleep(1)

    if (ends - begins)%5 != 0:
        ts = threading.Thread(target=main0, args=(end_page,ends))
        ts.start()
        print("线程数：", len(threading.enumerate()))



if __name__ == '__main__':
    main()


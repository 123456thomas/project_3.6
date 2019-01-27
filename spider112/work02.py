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

"""2、内涵段子爬虫(re)
https://www.neihan8.com/article/index.html
提取段子的：
标题，url，点赞数，踩数，浏览数，内容"""

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
爬取新闻标题，url，keywords
https://www.neihan8.com/article/index.html
"""


import re, requests, time
from lxml import etree

# 导入数据库
import pymysql

# 导入多线程和队列
import threading,random
from multiprocessing import Manager


def Web_get(urls):
    """
    获取页面的源码
    :param urls:
    :return:
    """
    time.sleep(random.random())
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    response = requests.get(urls, headers=headers)
    html = response.content.decode("utf8",'ignore')
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
    print(400)
    result1 = args[0].finditer(html)
    for li in result1:
        temp = li.group()
        print(temp)
        result2 = []
        for i in range(1,len(args)):
            try:
                temp2 = args[i].search(temp)
                Temp = temp2.group(1).strip()
                print(Temp)
                result2.append(Temp)
            except:
                result2.append("")
            if len(Temp)>200:
                Temp = Temp[:200]
        mysql_inset("xiaohua", *result2)

def main0(bgeins,ends):
    baseurl = "https://www.neihan8.com/article/index"
    """<div class=news_item"""
    re_part = re.compile(r'<div class="text-column-item box box-790">.*?<div class="view" >.*?</div>.*?</div>.*?</div>', re.I|re.S)
    re_title = re.compile(r'<h3><a.*?>(.*?)</a>', re.I | re.S)
    re_urls = re.compile(r'<h3><a href="(.*?)"', re.I | re.S)
    content = re.compile(r'<div class="desc">(.*?)</div>', re.I | re.S)
    re_good = re.compile(r'<div.*?class="good".*?>(.*?)</div>', re.I | re.S)
    re_bad = re.compile(r'<div.*?class="bad".*?>(.*?)</div>', re.I | re.S)
    re_num = re.compile('<div.*?class="view".*?>(.*?)</div>', re.I | re.S)
    args = (re_part, re_title, re_urls, content, re_good, re_bad, re_num)
    # 获取页面
    print(0000,1111)
    for t in range(bgeins,ends+1):
        if t != 1:
            newurl = baseurl + "_%s.html"%t
        else:
            newurl = baseurl + ".html"
        html = Web_get(newurl)
        # 正则匹配获取数据
        Spider_data(html, *args)

def main():
    # 翻页大于2页
    begins = int(input("起始页:"))
    ends = int(input("终止页页:"))
    try:
        # 多线程处理,一个线程1页
        for t in (begins,ends+1,5):
            if t +4>ends:
                end_page = t
                break
            #  每个线程处理5页
            ts = threading.Thread(target=main0, args=((t,t+4)),)
            ts.start()
            print("线程数：", len(threading.enumerate()))
            # 控制线程数,最多为4
            while len(threading.enumerate())>10:
                time.sleep(1)
        if (ends - begins)%4 != 0:
            ts = threading.Thread(target=main0, args=(end_page,ends))
            ts.start()
            print("线程数：", len(threading.enumerate()))
    except Exception as e:
        print(e)



if __name__ == '__main__':
    main()

"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/9/25'
# 需求：提取每一个帖子里面的用户头像的链接，用户名，段子的内容，点赞数，评论数
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


# 爬虫所需模块
from urllib import request,parse
from lxml import etree
import os,chardet

# 加载页面内容模块
import requests

# 写入异常的模块
import traceback,time

# 导入多线程和队列
import threading
from multiprocessing import Manager

# 抓起糗事百科页面
def Web_spider(url_,que,i):
    """
    页面抓取
    :return:
    """
    # 设置请求头
    headers = {'User-Agent': "Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)"}

    if i != 1:
        urls = url_ + "8hr/page/%s"%i
    else:
        urls = url_
    # 获取页面
    req = request.Request(urls, headers=headers)
    response = request.urlopen(req)
    try:
        response = request.urlopen(req)
    except:
        print("出错了")
    html = response.read()
    # html = html.decode("utf8", 'ignore')
    charset = chardet.detect(html)['encoding']
    que.put(html)
    print(charset)


# 抓取页面信息
def Spider_cont(que):
    """
    页面信息提取
    :param html:
    :return:
    """
    # 漏读条数
    t_num = 0
    html = que.get()
    Html = etree.HTML(html)
    result = Html.xpath("//div[contains(@class,'recommend-article')]/ul/li[contains(@class,'item')]")
    result_cl = Html.xpath("//div[contains(@class,'recommend-article')]/ul/li[contains(@class,'item')]/@class")
    result_sl = set(result_cl)
    print(result)
    print(result_sl)
    for i in result:
        try:
            result_link = i.xpath("./div[contains(@class,'recmd-right')]/a/@href")[0]
            title = i.xpath("./div[contains(@class,'recmd-right')]/a/text()")[0]
            focus = i.xpath(".//div[contains(@class,'recmd-num')]/span[1]/text()")[0]
            ans = i.xpath(".//div[contains(@class,'recmd-num')]/span[last()-1]/text()")[0]
            auth = i.xpath("./div[contains(@class,'recmd-right')]//span[contains(@class,'recmd-name')]/text()")[0]
        except:
            pass
        # 写入统计文本
        print(result_link)
        print(focus, ans)
        with open("qiushi/qiushi.json",'a',encoding='utf8') as f_w1:
            f_w1.write("\ntitle: " + title + "\n")
            f_w1.write("focus: " + focus + "\n")
            f_w1.write("ans: " + ans + "\n")
            f_w1.write("auth: " + auth + "\n\n")
            f_w1.write("^ ^"*60)

        t_num += 1


def main():
    urls = "https://www.qiushibaike.com/"
    que = Manager().Queue(5)
    try:
        for i in range(1,11):
            if len(threading.enumerate()) <6:
                ts_put = threading.Thread(target=Web_spider, args=((urls,que,i)))
                ts_get = threading.Thread(target=Spider_cont, args=((que,)))
                ts_put.start()
                ts_get.start()
                print(threading.enumerate())
            else:
                while len(threading.enumerate()) >= 6:
                    time.sleep(3)
    except Exception as e:
        print(e)
        with open('qiushi/error01.txt','a',) as f_er:
            # 写入错误信息
            traceback.print_exc(file=f_er)
            tim1 = time.localtime()
            tim1 = time.strftime("%Y-%m-%d %H:%M:%S", tim1)
            f_er.write("Report_time:"+tim1+'\n\n')



if __name__ == '__main__':
    main()

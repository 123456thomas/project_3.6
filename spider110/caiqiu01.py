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

"""

4、双色球历史数据爬虫，爬取期数，开奖时间，红色球，蓝色球，一等奖，二等奖等信息
http://zst.aicai.com/ssq/openInfo/
"""

from urllib import request,parse
import chardet, os
import http.cookiejar
from lxml import etree
import pymysql

def mysql_inset(name, ends, *datalist):
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
    # 3.1创建表
    try:
        query0 = "show tables"
        cur.execute(query0)
        result0 = cur.fetchall()
        if (name,) not in result0:
            query_ = "create table %s"%name
            query_ = query_ + "(id int primary key auto_increment,"\
                                             "期数 varchar(40) not null," \
                                             "日期 varchar(40) not null," \
                                             "红球 varchar(40) not null," \
                                             "蓝球 varchar(40) not null," \
                                             "总投注额 varchar(40) not null," \
                                             "一等奖注数 varchar(40) not null," \
                                             "一等奖奖金 varchar(40) not null," \
                                             "二等奖注数 varchar(40) not null," \
                                             "二等奖奖金 varchar(40) not null," \
                                             "奖池滚存 varchar(40) not null)"
            cur.execute(query_)
            print(con,cur)
            con.commit()
        # 3.2插入数据
        try:
            query2 ="insert into %s"%name
            query2 = query2 + " values(0,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cur.execute(query2, datalist)
            if con is not None:
                con.commit()
        except Exception as e:
            print(e)
    except Exception as e:
        print(e)
    finally:
        if ends == True:
            cur.close()
            con.close()
            print("=================")


def Web_get():
    """
    获取页面
    :return: 字节数据
    """
    # 1.创建请求头
    headers = {}
    headers[
        'Cookie'] = 'JSESSIONID=E48555420F2C6F169EA9BDF3F198F437.c54; UM_distinctid=168357d91335a-083780cb18fdb6-b781636-100200-168357d913516d; CNZZDATA3538029=cnzz_eid%3D120329851-1547084640-%26ntime%3D1547084640; Hm_lvt_49024937a7f937de669432245102dac6=1547085648; Hm_lpvt_49024937a7f937de669432245102dac6=1547085648'
    headers[
        'User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'

    # 1.创建cookie对象
    cookie = http.cookiejar.CookieJar()

    # 2.创建cookie处理器
    cookie_handler = request.HTTPCookieProcessor(cookie)

    # 3.创建开启器
    opener = request.build_opener(cookie_handler)
    opener.addheaders = [('Cookie','UM_distinctid=168357d91335a-083780cb18fdb6-b781636-100200-168357d913516d; CNZZDATA3538029=cnzz_eid%3D120329851-1547084640-%26ntime%3D1547084640; Hm_lvt_49024937a7f937de669432245102dac6=1547085648; JSESSIONID=2E0D60996E110532DE844A4C2C5449FB.c54; Hm_lpvt_49024937a7f937de669432245102dac6=1547085690'),
                         ('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36')]

    # 4.获取响应
    response = opener.open("http://zst.aicai.com/ssq/openInfo/")
    html = response.read()
    return html

def Spioder_date(html):
    """
    通过读取的页面抓取数据
    :param html:
    :return:
    """

    Html = etree.HTML(html)
    trs = Html.xpath("//table[contains(@class,'fzTab nbt')]/tbody/tr[position()>2]")
    print(len(trs))
    with open('files/caiseqiu.txt', 'w', encoding='utf8') as f_w:
        f_w.write('期数' + '\t')
        f_w.write('日期' + '\t'*2)
        f_w.write('红球' + '\t'*2)
        f_w.write('蓝球' + '\t')
        f_w.write('总投注额' + '\t')
        f_w.write('一等奖注数' + '\t')
        f_w.write('一等奖奖金' + '\t')
        f_w.write('二等奖注数' + '\t')
        f_w.write('二等奖奖金' + '\t')
        f_w.write('奖池滚存' + '\t\n')
    # 遍历结束表示
    Ends = False
    for tr in trs:
        qishu = tr.xpath("./td[1]/text()")[0]
        riqi = tr.xpath("./td[2]/text()")[0]
        reds = tr.xpath("./td[2<position() and position()<9]/text()")
        # 将红球拼接
        red = " ".join(reds)
        blue = tr.xpath("./td[9]/text()")[0]
        sumtou = tr.xpath("./td[10]/text()")[0]
        zhu1 = tr.xpath("./td[11]/text()")[0]
        jiang1 = tr.xpath("./td[12]/text()")[0]
        zhu2 = tr.xpath("./td[13]/text()")[0]
        jiang2 = tr.xpath("./td[14]/text()")[0]
        chizi = tr.xpath("./td[last()]/text()")[0]
        # print(qishu,riqi,red,blue,sumtou,zhu1,jiang1,zhu2,jiang2,chizi)
        with open('files/caiseqiu.txt','a',encoding='utf8') as f_w:
            f_w.write("\n" + qishu + '\t')
            f_w.write(riqi + '\t')
            f_w.write(red + '\t')
            f_w.write(blue + '\t')
            f_w.write(sumtou + '\t')
            f_w.write(zhu1 + '\t')
            f_w.write(jiang1 + '\t')
            f_w.write(zhu2 + '\t')
            f_w.write(jiang2 + '\t')
            f_w.write(chizi + '\t')
        # 数据库存储
        if tr == trs[-1]:
            Ends = True
        rows_data = [qishu, riqi, red, blue, sumtou, zhu1,
                jiang1, zhu2, jiang2, chizi]
        mysql_inset('caiseqiu', Ends, *rows_data)


def main():
    html = Web_get()
    Spioder_date(html)


if __name__ == '__main__':
    main()
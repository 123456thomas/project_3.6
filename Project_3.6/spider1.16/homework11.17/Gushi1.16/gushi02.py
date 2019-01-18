"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/9/25'
# http://vip.stock.finance.sina.com.cn/mkt/
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
"""json数据：
amount: 271145
buy: "4.980"
changepercent: "1.212"
code: "200011"
high: "5.020"
low: "4.950"
mktcap: 298585.525092
name: "深物业B"
nmc: 33870.226743
open: "4.950"
pb: 1.035
per: 4.793
pricechange: "0.060"
sell: "5.010"
settlement: "4.950"
symbol: "sz200011"
ticktime: "15:00:03"
trade: "5.010"
turnoverratio: 0.08032
volume: 54300

请求头数据：
page: 1 ，2
num: 40
sort: symbol
asc: 1
node: sh_b ， sh_a ，sz_a， sz_b
symbol: 
_s_r_a: init


"""

# 导入页面请求
import requests,pymysql
import time, json,re
# 导入动态资源加载模块
from selenium import webdriver
import threading

Ends_ = False
def mysql_inset(name, ends, *datalist):
    """
    在spider数据库中，创建表，并插入数据
    :param name:表名
    :param datalist:一条数据的列表形式
    :param ends:写入结束，关闭数据库
    :return:
    """
    global Ends_
    # 1.构建连接对象
    con = pymysql.connect(host="localhost",
                          user="root",
                          password="361365",
                          database="stocks",
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
                                             "代码 varchar(255) not null," \
                                             "名称 varchar(255) not null," \
                                             "最新价 varchar(255) not null," \
                                             "涨跌额 varchar(255) not null," \
                                             "涨跌幅 varchar(255) not null," \
                                             "买入 varchar(255) not null," \
                                             "卖出 varchar(255) not null," \
                                             "昨收 varchar(255) not null," \
                                             "今开 varchar(255) not null," \
                                             "最高 varchar(255) not null,"\
                                             "最低 varchar(255) not null,"\
                                             "成交量_手 varchar(255) not null,"\
                                             "成交额_万 varchar(255) not null)"
            cur.execute(query_)
            print(con,cur)
            con.commit()
        # 3.2插入数据
        try:
            query2 ="insert into %s"%name
            query2 = query2 + " values(0,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cur.execute(query2, datalist)
            if con is not None:
                con.commit()
                cur.close()
                con.close()
                print("=================")
        except Exception as e:
            print(e)
    except Exception as e:
        print(e)



def web_get(url_, ends_, i, num1):
    global Ends_
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"}
    # 1.构建webdriver实例获取页面
    param = {"page": str(num1), "sort": "symbol","num": "40", "asc": "1", "symbol": "","node": i, "_s_r_a": "init"}
    response = requests.get(url_, headers=headers, params=param)
    web_num = 0
    while True:
        if response.status_code == 200:
            one_re = re.compile(r"{(.*?)}", re.I|re.S)
            one_sym = re.compile(r'symbol:"(.*?)"', re.I|re.S)  # 代码
            name_re = re.compile(r'name:"(.*?)"', re.I|re.S)  # 名称
            sell_re = re.compile(r'sell:"(.*?)"', re.I|re.S)  # 最新价
            prich_re = re.compile(r'pricechange:"(.*?)"', re.I|re.S)  # 涨跌额
            chaper_re = re.compile(r'changepercent:"(.*?)"', re.I|re.S)  # 涨跌幅
            buy_re = re.compile(r'buy:"(.*?)"', re.I|re.S)  # 买入
            trade_re = re.compile(r'trade:"(.*?)"', re.I|re.S)  # 卖出
            settle_re = re.compile(r'settlement:"(.*?)"', re.I|re.S)  # 昨收
            open_re = re.compile(r'open:"(.*?)"', re.I|re.S)  # 今开
            high_re = re.compile(r'high:"(.*?)"', re.I|re.S)  # 最高
            low_re = re.compile(r'low:"(.*?)"', re.I|re.S)  # 最低
            vol_re = re.compile(r'volume:(.*?),', re.I|re.S)   # 成交量，手
            amount_re = re.compile(r'amount:(.*?),', re.I|re.S)  # 成交额，万
            data = response.text[1:-1]
            # one_lis = one_re.finditer(data)
            print("data",len(data))
            if len(data) < 4:
                print("data",data)
                ends_ = True
                Ends_ = True
            one_lis = one_re.findall(data)
            for item in one_lis:
                # li_one = item.group()
                li_one = item
                print(li_one)
                symbol = one_sym.search(li_one).group(1)
                name = name_re.search(li_one).group(1)
                sell = sell_re.search(li_one).group(1)
                prich = prich_re.search(li_one).group(1)
                chaper = chaper_re.search(li_one).group(1)
                buy = buy_re.search(li_one).group(1)
                trade = trade_re.search(li_one).group(1)
                settle = settle_re.search(li_one).group(1)
                open = open_re.search(li_one).group(1)
                high = high_re.search(li_one).group(1)
                low = low_re.search(li_one).group(1)
                vol = int(vol_re.search(li_one).group(1))
                vol = str(vol//100)
                amount = int(amount_re.search(li_one).group(1))
                amount = str(amount//100/100)
                print(symbol,name,sell,prich,chaper,buy,trade,settle,open,high,low,vol,amount)
                datalist = [symbol,name,sell,prich,chaper,buy,trade,settle,open,high,low,vol,amount]
                print(1000222)
                print(datalist)
                print(ends_, len(data))
                mysql_inset(i, ends_, *datalist)
            print("你好")
            return True
        else:
            if web_num > 9:
                print('网络超时，或无效地址')
                return False
            time.sleep(5)
            web_num += 1
            print("响应中....")
        print("响应中2....")


def main():
    global Ends_
    ends_ = False
    baseurl = "http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData"
    gu_list = ["sz_a", "sz_b", "sh_a", "sh_b"]
    # 股票市场迭代
    for i in gu_list:
        num1 = 1
        Ends_ = False
        while True:
            # 多线程处理
            #  每个线程处理1页
            if Ends_ == False:
                ts = threading.Thread(target=web_get, args=((baseurl,ends_, i, num1)), )
                ts.start()
            print("线程数：", len(threading.enumerate()))
            # 控制线程数,最多为4
            while len(threading.enumerate()) > 20:
                time.sleep(1)
            num1+=1
            print("现有线程数：", len(threading.enumerate()))
            if len(threading.enumerate())==1:
                print("下一项")
                time.sleep(6)
                break


if __name__ == '__main__':
    main()
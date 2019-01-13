"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/9/25'
# 抓取西刺网代理ip：http://www.kuaidaili.com/free/inha/
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

from urllib import request,parse
import zlib
from lxml import etree
import pymysql ,os ,chardet, requests
from bs4 import BeautifulSoup

# 1.网页抓取
def Web_get(urls):
    """
    页面抓取
    :param urls:
    :return: 返回页面流
    """
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0"}
    response = requests.get(urls, headers=headers)
    html = response.content
    return html

def Spider_data(html, nametxt, tag, *attr):
    soup = BeautifulSoup(html,'lxml')
    lists = []
    listn = []
    for m in tag:
        a_tag = soup.select(m)
        for i in a_tag:
            # attr可能含href或src
            href0 = ""
            for t in attr:
                href0 += i.get(t)
            name0 = i.get_text()
            with open('files/%s.txt'%nametxt, 'a', encoding='utf8') as f:
                f.write('\n' +name0 +'\n')
                f.write(href0)
            lists.append(href0)
            listn.append(name0)
    return [lists,listn]


def main():
    baseurl = "http://www.kuaidaili.com/free/inha/"
    html = Web_get(baseurl)
    # 获取ip、port信息
    tags = ['tbody>tr>td[data-title="IP"]',
            'tbody>tr>td[data-title="PORT"]']
    lisB1,lisB2 = Spider_data(html,"agent_ip",tags)
    lang =int(len(lisB2) / 2)
    for i in range(lang):
        with open('files/agentIp.txt', 'a', encoding='utf8') as f:
            f.write(lisB2[i]+":"+lisB2[i+lang]+ '\n')

if __name__ == '__main__':
    main()
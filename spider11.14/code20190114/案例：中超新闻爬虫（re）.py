"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2019/1/14'
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
from urllib import request
import chardet
import re


def down(url):
    '''
    根据url请求指定的页面
    :param url:
    :return:
    '''
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)'}
    req = request.Request(url,headers=headers)
    response = request.urlopen(req)
    html = response.read()
    charset = chardet.detect(html)
    html = html.decode(charset['encoding'],errors='ignore')
    return html


if __name__ == '__main__':
    url = 'http://sports.163.com/zc/'
    html = down(url)
    #print(html)
    # 新闻条目
    pat_1 = re.compile(r'<div class="news_item">(.*?</div>.*?<div class="share">)',re.M|re.S)
    # 新闻标题
    pat_2 = re.compile(r'<h3>.*?<a.*?>(.*?)</a>',re.M|re.S)
    # 新闻url
    pat_3 = re.compile(r'<h3>.*?<a href="(.*?)"',re.M|re.S)
    # 新闻标签
    pat_4 = re.compile(r'<div class="keywords">(.*?)</div>',re.M|re.S)
    # 标签文本
    pat_5 = re.compile(r'<a.*?>(.*?)</a>',re.M|re.S)
    # 跟帖数
    pat_6 = re.compile(r'<div class="share_join">.*?<span class="icon">(.*?)</span>',re.M|re.S)

    ls = pat_1.findall(html)
    print(ls)
    print(len(ls))

    for item in ls:
        matObject = pat_2.search(item)
        if matObject != None:
            title = matObject.group(1)
        else:
            title = "空"
        print('title:',title)
        matObject = pat_3.search(item)
        if matObject != None:
            news_url = matObject.group(1)
        else:
            news_url = "空"
        print('news_url:',news_url)

        matObject = pat_4.search(item)
        if matObject != None:
            tagstr = matObject.group(1)
            tagls = pat_5.findall(tagstr)
            if len(tagls)>0:
                tags = ' '.join(tagls)
            else:
                tags = '空'
        else:
            tags = "空"
        print('tags:',tags)

        matObject = pat_6.search(item)
        if matObject != None:
            comments = matObject.group(1)
        else:
            comments = "0"
        print('comments:', comments)
        print('='*60)












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

from urllib import request,parse

# 导入xpath解析模板
from lxml import etree
import requests
import chardet,os

# 设置请求头
headers = {"User-Agent": 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'}
urls = "https://tieba.baidu.com/f?"
search = input("贴吧搜索：")
while True:
    try:
        search_num1 = int(input("起始贴吧页数："))
        search_num2 = int(input("终止贴吧页数："))
        if search_num1>search_num2:
            tem = search_num1
            search_num1 = search_num2
            search_num2 = tem
        break
    except:
        pass
search = parse.urlencode({"kw": search})
urls = urls + search
baseurl = "https://tieba.baidu.com"
if not os.path.exists("tieba"):
    os.mkdir('tieba')
if not os.path.exists("tieba/imgs"):
    os.mkdir('tieba/imgs')
# 图片名字全局变量
snum=0
for i in range(search_num1,search_num2+1):
    # 抓取页面
    page ="&pn=" + str((i-1)*50)
    urlss = urls + page
    print(urlss)
    req = request.Request(urlss, headers=headers)
    print(req)
    try:
        response = request.urlopen(req)
    except:
        break
    # 读取并存取数据
    html =response.read()
    charset = chardet.detect(html)['encoding']
    print(charset)
    html = html.decode("utf8",'ignore')
    Html =etree.HTML(html)
    result = Html.xpath('//li[contains(@class,"j_thread_list clearfix")]')
    # 遍历当前页的帖子
    for i in result:
        title = i.xpath(".//div[contains(@class,'threadlist_title pull_left j_th_tit ')]/a[contains(@class,'j_th_tit ')]/@title")[0]
        href = i.xpath(".//div[contains(@class,'col2_right j_threadlist_li_right')]//a[contains(@class,'j_th_tit ')]/@href")[0]
        visit_num = i.xpath(".//span[contains(@class,'threadlist_rep_num center_text')]/text()")[0]
        auth = i.xpath(".//span[contains(@class,'tb_icon_author ')]/@title")[0]
        print(title)
        print(auth)
        print(visit_num)
        print(href)
        Urls = baseurl +href
        with open('tieba/news.txt','a',encoding='utf8') as f_w:
            f_w.write("title:"+title + '\n')
            f_w.write("auth:"+auth + '\n')
            f_w.write("visit_num:"+visit_num + '\n')
            f_w.write("Urls:"+Urls + '\n')
        # BDE_Image
        # 帖子图片抓取
        reqs = request.Request(Urls, headers=headers)
        responses = request.urlopen(reqs)
        # 读取并存取数据
        htmls = responses.read()
        htmls = htmls.decode("utf8")
        Htmls = etree.HTML(htmls)
        results = Htmls.xpath('//div[contains(@class,"d_post_content j_d_post_content ")]//img[contains(@class,"BDE_Image")]/@src')
        print(results)
        # 写图片，错误文档
        # 帖子编码
        try:
            for s in range(len(results)):
                r = requests.get(results[s])
                with open("tieba/imgs/"+str(snum).zfill(4)+str(s).zfill(2)+".jpg",'wb') as f:
                    f.write(r.content)
        except Exception as e:
            print(e)
            with open('tieba/error.txt','a',encoding='utf8') as f_w1:
                f_w1.write(title+'\n')
                f_w1.write('图片数目:'+str(len(results))+'\n')
                f_w1.write(str(e))
                f_w1.write("\n")
        snum += 1
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

# 抓起糗事百科页面
def Web_spider(url_, begins, ends):
    """
    页面抓取
    :return:
    """

    # 设置请求头
    headers = {'User-Agent': "Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)"}
    for i in range(begins, ends+1):
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
            break
        html = response.read()
        # html = html.decode("utf8", 'ignore')
        charset = chardet.detect(html)['encoding']
        print(charset)
        return html

# 抓取页面信息
def Spider_cont(html):
    """
    页面信息提取
    :param html:
    :return:
    """
    # 漏读条数
    t_num = 0
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
        with open("qiushi/qiushi.txt",'a',encoding='utf8') as f_w1:
            f_w1.write("\ntitle: " + title + "\n")
            f_w1.write("focus: " + focus + "\n")
            f_w1.write("ans: " + ans + "\n")
            f_w1.write("auth: " + auth + "\n\n")
            f_w1.write("^ ^"*60)

        # 进入新链接
        newurl = "https://www.qiushibaike.com" + result_link
        newhtml = Web_spider(newurl, 1, 1)
        Htmls = etree.HTML(newhtml)
        content = Htmls.xpath("//div[contains(@class,'article block untagged noline')]//div[contains(@class,'content')]/text()")
        imgs = Htmls.xpath("//div[contains(@class,'article block untagged noline')]//img/@src")
        gifs = Htmls.xpath("//div[contains(@class,'article block untagged noline')]//img[contains(@src,'/gif/')]/@src")
        source = Htmls.xpath("//div[contains(@class,'article block untagged noline')]//source/@src")

        print(content)
        print(t_num,len(result))
        # 写入文章
        for s in range(len(content)):
            filname = "qiushi/text/" + str(t_num) + "%s.txt"%s
            print(content[s])
            with open(filname, "w",encoding='utf8') as f_c:
                f_c.write(content[s])
        # 载入图片
        try:
            for s in range(len(imgs)):
                filname = "qiushi/imgs/" + str(t_num) + "%s.jpg"%s
                rimg = requests.get(imgs[s])
                with open(filname, "wb") as f_i:
                    f_i.write(rimg.content)
        except:
            pass
        # 载入图片gif
        for s in range(len(gifs)):
            filname = "qiushi/gifs/" + str(t_num) + "%s.gif"%s
            rgif = requests.get(gifs[s])
            with open(filname, "wb") as f_g:
                f_g.write(rgif.content)
        # 载入视频
        print(source)
        for s in range(len(source)):
            filname = "qiushi/mp4/" + str(t_num) + "%s.mp4" % s
            with requests.get(source[s], stream=True) as f_v:
                chunck_size = 10240
                cont_size = int(f_v.headers['content-length'])
                with open(filname,'wb') as f_vs:
                    for chunk in f_v.iter_content(chunk_size=chunck_size):
                        f_vs.write(chunk)
                    print('%s加载完成'%filname)
        t_num += 1





    # https://www.qiushibaike.com/ 首页
    # https: // www.qiushibaike.com / 8 hr / page / 3 /
    # http: // www.jokeji.cn / jokehtml / bxnn / 20090926220449.htm

def main():
    urls = "https://www.qiushibaike.com/"
    try:
        html = Web_spider(urls,1,1)
        Spider_cont(html)
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

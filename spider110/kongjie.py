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

import requests
from bs4 import BeautifulSoup

# 1.网页抓取
def Web_get(urls):
    """
    获取页面
    :return: 字节数据
    """
    # 1.创建请求头
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'

  # 4.获取响应
    response = requests.get(urls)
    html = response.text
    return html

# 数据抓取
def Spider_data(html, **tagattrs):
    """
    榨取页面信息
    :param html:
    :param tagattrs: 为标签使用css定位,属性（href 、src、None)
    :return: 二元元组
    """
    soup = BeautifulSoup(html,'lxml')
    tags = []
    for tag, attr in tagattrs.items():
        a_tag = soup.select(tag)
        temp = []
        for atag in a_tag:
            try:
                srcs = atag.select('img')[0].attrs['src']
                if srcs == "static/image/common/nopublish.gif":
                    continue
            except:
                pass

            a_link = atag.attrs[attr]
            temp.append(a_link)
        tags.append(temp)
    return tags

# 相册翻页
def down_s(html, attrs,urls,ret):
    """

    :param urls:
    :param attrs:
    :return: 各业相册列表
    """
    soup = BeautifulSoup(html, 'lxml')
    page = 1
    try:
        sum_page = soup.select(attrs)[0]
        sum_page = sum_page.get_text().strip()
        sumpage = int(sum_page.strip()[1:-1])
        for i in range(1,sumpage+1):
            newurl = urls + ret%i
            yield newurl
    except:
        yield urls


def fun2(x):
    y = x.split(".thumb.jpg")[0]
    return y

def main():
    baseurl = "http://www.kongjie.com/home.php?mod=space&do=album&view=all&page="
    tagattr= {}
    tagattr['.ml.mla.cl>li>div>a'] = "href"
    # 相片翻页 &page=1#comment
    taga = '.pgs.cl.mtm>.pg>label>span'
    # 相片特征
    tagattr1 = {}
    tagattr1['.ptw.ml.mlp.cl>li img'] = "src"


    # 翻页
    begins = int(input("起始页:"))
    ends = int(input("终止页页:"))
    nums = 0
    # 获取页面
    for i in range(begins,ends+1):
        newurl = baseurl +str(i)
        html =Web_get(newurl)
        bulmurl = Spider_data(html,**tagattr)
        print(bulmurl)
        # 获取相册相面
        for t in bulmurl[0]:
            html = Web_get(t)
            bulmur2 = down_s(html, taga, t, "&page=%s#comment")
            for u in bulmur2:
                # 到每页中提取用户图片url
                print(u)
                html3 = Web_get(u)
                imgurls = Spider_data(html3,**tagattr1)

                lis2 = map(fun2, imgurls[0])
                for st in lis2:
                    dataimg = requests.get(st)
                    with open("files/imgs/a%s.jpg"%nums,'wb') as f:
                        f.write(dataimg.content)
                    nums += 1
    print(nums)

if __name__ == '__main__':
    main()
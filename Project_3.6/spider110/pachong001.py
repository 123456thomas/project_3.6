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
1、医疗器械网爬虫
http://www.chinamedevice.cn/
以医疗产品分类下的外科器械，康复护理设备器具，口腔科设备等大的分类为入口，爬取医疗产品
使用 BeautifuSoup4 解析器进行数据提取，提取产品名称，产品url，封面url，产品类别，批准文号，产品规格，产品说明
产品说明，联系人，联系电话，移动电话，单位地址
保存到mysql数据库中
"""

# 0.导入模块
from bs4 import BeautifulSoup
from urllib import request,parse
import zlib
from lxml import etree
import pymysql ,os ,chardet, requests

# 如果ip被禁，更换代理ip
def Agent_id():
    # 定义代理地址
    proxy = {'http': "211.159.219.225:8118"}

    # 创建代理处理器对象
    proxy_handler = request.ProxyHandler(proxy)

    # 创建opener对象
    opener = request.build_opener(proxy_handler)

    # 安装opener
    request.install_opener(opener)

# 1.网页抓取
def Web_get(urls):
    """
    页面抓取
    :param urls:
    :return: 返回页面流
    """
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
    # 方法1：
    # req = request.Request(urls, headers=headers)
    # response = request.urlopen(req)
    # html = response.read()
    # # 为保证之后数据榨取时，不丢失标签，最好获取编码方式，解码
    # charset = chardet.detect(html)['encoding']
    # print(charset)
    # html = html.decode(charset,'ignore')

    # 方法2：
    response = requests.get(urls,headers=headers)
    html = response.text
    return html


# 2.页面数据榨取
def Spider_data(html, nametxt, *tag ,**param):
    """
    页面数据榨取
    :param html: 页面流
    :param attr: href或src
    :param nametxt: 保存的文件名，存储链接内容和url
    :param tag: 标签css属性
    :param param: 标签属性和值
    :return:url 内容的二元列表
    """
    lists = []  # 存储url
    listn = []  # 存储text文本
    soup = BeautifulSoup(html,"lxml")
    for m in tag:
        a_tag = soup.select(m)
        for i in a_tag:
            # 提取超链接
            if "href" in i.attrs:
                href0 = i.get("href")
            elif "src" in i.attrs:
                href0 = i.get("src")
            else:
                href0 = ""
            # 提取内容
            try:
                name0 = i.get_text().strip()
            except:
                name0 = ""
            with open('files/%s.txt'%nametxt, 'a', encoding='utf8') as f:
                if name0 != "" :
                    f.write('\n' +name0)
                if href0 != "" :
                    f.write(href0 +'\n')
            lists.append(href0)
            listn.append(name0)
    return [lists,listn]


def main():
    baseurl = "http://www.chinamedevice.cn"
    # 抓取主页面
    html_main = Web_get(baseurl)
    # 超链接信息
    tag = ['.f12']
    with open('files/main.txt', 'w', encoding='utf8') as f:
        f.write('')
    listA= Spider_data(html_main,"main",*tag)
    print(len(listA[0]))
    # 抓取产品列表的页面
    with open('files/mainsort.txt', 'w', encoding='utf8') as f:
        f.write('')
    listBs = []
    for s in listA[0]:
        urlnew = baseurl +s
        html_main1 = Web_get(urlnew)
        # 超链接信息
        tag1 = ['li>h3>span>a']
        # 返回产品链接列表
        listB = Spider_data(html_main1, "mainsort", *tag1)
        listBs.extend(listB[0])

    # 抓取产品页面，并提取有用数据
    with open('files/goodsinfo.txt', 'w', encoding='utf8') as f:
        f.write('')
    tem = False
    for j in listBs:
        html_ware = Web_get(j)
        # 构建产品信息css
        ware_name = "h1"
        ware_img = ".img>a>img"
        ware_Category = ".text01>ul>li:nth-child(2)"
        ware_EngN = ".text01>ul>li:nth-child(3)"
        ware_Appr_Num = ".text01>ul>li:nth-child(4)"
        ware_Specific = ".text01>ul>li:nth-child(5)"
        ware_Descrip = ".text03>p,div"
        producter = 'li.bgwhite.pt>h3>a'
        contacter = ".text04>ul>li"
        phone = ".text04>li:nth-child(5)"
        address = ".text04>li:nth-child(9)"
        tag2 =[ware_name,  # 商品名
               ware_img,  # 商品封面
               ware_EngN,  # 商品英文名
               ware_Category,  # 商品类型
               ware_Appr_Num,  # 商品批准文号
               ware_Specific,  # 商品规格
               ware_Descrip,  # 商品说明
               producter,  # 生产企业
               contacter,  # 联系人
               phone,  # 联系方式
               address]
        # 返回产品信息
        listCs = Spider_data(html_ware, "goodsinfo", *tag2)

if __name__ == '__main__':
    main()



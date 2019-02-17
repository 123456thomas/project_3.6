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


import random, time
import requests,json
from lxml import etree
from fake_useragent import UserAgent
urls = 'https://www.jd.com/'
class Spider_jd:
    def __init__(self):
        pass

    def get_web(self, urls):
        """抓取数据"""
        ua = UserAgent()
        header = {'User-Agent':ua.random,
                  'Cookie':'__jdu=936530910; shshshfpa=ed3ea6f8-8fd5-e449-8559-ce3ebe433c3b-1547297784; shshshfpb=lte6M1mpgcQy1llcFCewFVg%3D%3D; __jdc=122270672; __jdv=122270672|direct|-|none|-|1550285463154; o2Control=webp; PCSYCityID=412; __jda=122270672.936530910.1547297767.1550307117.1550309946.6; ipLoc-djd=1-72-2799-0; shshshfp=a50303814c89b5221870a4dc13e3ca2f; user-key=d0fa314e-f9db-4a92-ae47-23fe24437e8b; cn=0'}
        # req = requests.Request(url=urls,headers=header)
        response = requests.get(urls,headers=header)
        html = response.text
        # print(html)
        return html

    def parse_date(self, html, xpaths,toge):
        """解析数据，获取目标"""
        Html = etree.HTML(html)
        for xpath in xpaths: # 尝试其中每种xpath，有一个满足即可退出
            result = Html.xpath(xpath)
            for res in result:
                try:
                    title = res.xpath('./text()')
                    href = res.xpath('./@href')
                    if len(title)>0:
                        title = title[0].strip()
                    if len(href)>0:
                        href = href[0]
                        if href[:4] != 'http':
                            href = 'https:' + href
                    print('toge',toge)
                    if toge==1:
                        print('++++  ===')
                    print('title=', title)
                    print('href=', href)
                    yield [title,href]
                except Exception as e:
                    print(html.title())
                    print('出错啦')
                    time.sleep(3)
            if len(result)!=0 and toge==-1:
                break


    def parse_deep(self,start_url, rules):
        """深度爬取，知道爬完所有规则，深度为len(rules)"""
        print(rules)
        html =self.get_web(start_url)
        print(rules[0][0])
        result = self.parse_date(html,rules[0][1],rules[0][0])
        if len(rules)<=1:
            return
        for m,n in result:
            print('===:',n)
            self.parse_deep(n,rules[1:])



def main():
    # //*[@id="J_goodsList"]/ul/li[1]/div/div[1]/a
    # //*[@id="J_goodsList"]/ul/li[1]/div/div[1]/a
    # //*[@id="plist"]/ul/li[2]/div/div[1]/a
    # //*[@id="root"]/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[1]/div/div/div[2]/span[1]/a
    # //*[@id="root"]/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[2]/div/div/div[2]/span[1]/a
    # //div[class="tab o2_fs_nav_tab"]/div[1]//div[2]/span/a
    # //*[@id="J_goodsList"]/ul/li[1]/div/div[1]/a
    # /html/body/div[6]/div/div[2]/div[1]
    # //div[class="sku-name"]
    # //div[class="itemInfo-wrap"]/div[3]//span[class="p-price"]/span[2]
    # //div[class="score-parts"]/div[1]/span[2]/em
    rules = [[-1,['//div[@id="J_cate"]/ul/li[5]/a']],
             [-1,['/html/body/div[5]/div/div[1]//dd//a',
              '//div[class="tab o2_fs_nav_tab"]/div[1]//div[2]/span/a']],
             [-1,['//*[@id="J_goodsList"]/ul/li/div/div[1]/a',
              '//*[@id="plist"]/ul/li/div/div[1]/a']],
             [1,['//div[class="sku-name"]',
              '//div[class="itemInfo-wrap"]/div[3]//span[class="p-price"]/span[2]',
              '//div[class="score-parts"]/div/span/em']]
             ]
    spide = Spider_jd()
    spide.parse_deep(urls, rules)



if __name__ == '__main__':
    main()

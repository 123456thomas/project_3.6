"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/7/23'
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
import re
import pymongo


class KongjieSpider:
    def __init__(self):
        server = 'localhost'
        port = '27017'
        dbname = 'admin'
        user = 'admin'
        pwd = '123'
        uri = 'mongodb://' + user + ':' + pwd + '@' + server + ':' + port + '/' + dbname
        client = pymongo.MongoClient(uri)  ##与MongDB建立连接
        db = client['dbkongjie']  ## 选择一个数据库
        self.kongjie_collection = db['kongjie']  ##在数据库中，选择一个集合


    def getUA(self):
        user_agent = 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'
        headers = {'User-Agent': user_agent}
        return headers


    def parse_album_url(self,url):
        """
        解析出相册url，然后进入相册爬取图片
        """
        headers = self.getUA()
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        people_list = soup.select('div.ptw > ul > li')
        for people in people_list:
            self.save_images_in_album(people.div.a['href'])

        #爬取下一页
        next_page = soup.select_one('a.nxt')
        if next_page:
            self.parse_album_url(next_page['href'])
        else:
            print('下载结束！')


    def save_images_in_album(self,album_url):
        """
        进入空姐网用户的相册，开始一张一张的保存相册中的图片。
        """
        headers = self.getUA()
        response = requests.get(album_url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        ls = soup.select('ul.ptw.ml.mlp.cl > li')
        if len(ls)>0:
            print('len ',len(ls))
            for item in ls:
                # 提取照片页面的url
                url = item.select_one('a')['href']
                #去重操作
                if self.kongjie_collection.find_one({'img_url': url}):  ##判断这个主题是否已经在数据库中、不在就运行else下的内容，在则忽略。
                    print(u'这个页面已经爬取过了')
                else:
                    pat = re.compile(r'uid=(\d+)&.*?picid=(\d+)')
                    matchObj = pat.search(url)
                    uid = matchObj.group(1)
                    picid = matchObj.group(2)
                    print('uid:',uid)
                    print('picid:',picid)
                    # 打开照片页面,提取image的src属性
                    response = requests.get(url, headers=headers)
                    soup1 = BeautifulSoup(response.text, 'lxml')
                    img_url = soup1.select_one('div#photo_pic > a > img')['src']
                    # 下载图片
                    response = requests.get(img_url, headers=headers)
                    imgName = './images/'+ uid + picid +'.jpg'
                    with open(imgName,'wb') as file:
                        file.write(response.content)
                    self.kongjie_collection.save({'img_url': url})

            ls = soup.select('a.nxt')
            print('next_page: ',len(ls))
            if len(ls)>0:
                next_page_url = ls[0]['href']
                print('next_page_url:',next_page_url)
                save_images_in_album(next_page_url)


if __name__ == '__main__':
    start_url='http://www.kongjie.com/home.php?mod=space&do=album&view=all&page=1'
    spider = KongjieSpider()
    spider.parse_album_url(start_url)




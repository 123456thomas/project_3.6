#                    _ooOoo_
#                   o8888888o
#                   88" . "88
#                   (| -_- |)
#                   O\  =  /O
#                ____/`---'\____
#              .'  \\|     |//  `.
#             /  \\|||  :  |||//  \
#            /  _||||| -:- |||||-  \
#            |   | \\\  -  /// |   |
#            | \_|  ''\---/''  |   |
#            \  .-\__  `-`  ___/-. /
#          ___`. .'  /--.--\  `. . __
#       ."" '<  `.___\_<|>_/___.'  >'"".
#      | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#      \  \ `-.   \_ __\ /__ _/   .-` /  /
# ======`-.____`-.___\_____/___.-`____.-'======
#                    `=---='
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#             佛祖保佑       永无BUG

import requests
import json
import urllib3
from lxml import etree

urllib3.disable_warnings()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Cookie': '_zap=e4c69db8-2dfb-4297-a38e-5b570f203604; _xsrf=FJOlMAJhAsqDK8NSTLApzEQeFlnhYBdX; d_c0="AFBjzCvo8Q6PTlbVQWyuddpyNqUM7BDSj9M=|1549532267"; q_c1=e7d0cd93220641f18e176549aedeb9dc|1549684664000|1549684664000; tst=r; tgw_l7_route=7bacb9af7224ed68945ce419f4dea76d; capsion_ticket="2|1:0|10:1549865043|14:capsion_ticket|44:Nzk1NDE5ZmM4ZDA1NGM4ZGI0OWIxMmNiYTA0NWJhZWQ=|921fd65a6ea41705443ed0cfb1c078b85c34a826364a0df9f2767164f5212210"; z_c0="2|1:0|10:1549865055|4:z_c0|92:Mi4xaUZvQ0N3QUFBQUFBVUdQTUstanhEaVlBQUFCZ0FsVk5YMTVPWFFEZlhMR2Vjb3B1NE9PRHBxcmRuOWhqbUJpNkZ3|00b25d6c97201a3958ecad12b59228982443fc1ec575c3960959c4d77d2df441"',
    #'Referer': 'https://www.zhihu.com/signup?next=%2F',
    #'Accept-Encoding': 'gzip, deflate',
    #'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    #'Accept-Language': 'zh-CN,zh;q=0.9',
    #'Connection': 'keep-alive',
}
url = 'https://www.zhihu.com/'
response = requests.get(url, headers=headers, verify=False)
html = response.text
print(html)
html = etree.HTML(html)
#print(etree.tostring(html, pretty_print=True).decode())
ls = html.xpath('//div[@class="Card TopstoryItem TopstoryItem-isRecommend"]')
print(len(ls))
for item in ls:
    title = item.xpath('.//h2//a/text()')[0]
    print(title)
    #url = item.xpath('.//h2//a/@href')[0]
    #print(url)
    brief = item.xpath('.//span[@class="RichText ztext CopyrightRichText-richText"]/text()')[0].strip()
    print(brief)
    print('=' * 60)

url = 'https://www.zhihu.com/api/v3/feed/topstory/recommend'
page_number = 2
limit = 6
after_id = 5
for page in range(2,15):
    params = {
        'session_token': '8849a419c97696924400be64eae21778',
        'desktop': 'true',
        'page_number': page_number,
        'limit': limit,
        'action': 'down',
        'after_id': after_id,
    }
    print('test...')
    data=requests.get(url=url,headers=headers,params=params,verify=False).text
    data = json.loads(data)['data']
    for item in data:
        #print(item)
        title = '无'
        if 'target' in item:
            if 'question' in item['target']:
                if 'title' in item['target']['question']:
                    title = item['target']['question']['title']
            elif 'title' in item['target']:
                title = item['target']['title']
        elif 'title' in item:
            title = item['title']
        print(title)
        brief = item['target']['excerpt']
        print(brief)
        print('=' * 60)
    page_number +=1
    after_id +=6

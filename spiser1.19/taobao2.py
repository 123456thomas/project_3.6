
from urllib import request

import requests,time

import chardet,json

base_url = 'https://www.taobao.com/markets/tbhome/cool-shop?spm=a21bo.7929913.198967.8.badc4174lVloNb&categoryId=2101'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
           }
param = {"jsv":'2.4.2',"appKey":'12574478',"t":'1548077499566',"sign":'20881c04f385f3e2aa7e3a5661aacc26',"api":'mtop.polaris.shop.getGoodShopRecommend',
         "v":'4.0',"dataType":'jsonp',"type":'jsonp',"callback":'mtopjsonp1',"data":{"cateId":"2101","size":15,"position":0,"count":5,"needTabs":'true',"algArgs":"","rpos":""}}
response = requests.get(base_url,headers=headers,params=param)

time.sleep(15)
while True:
    if response.status_code == 200:
        data = json.loads(response.text)["data"]
        print(data)
        # if len(data) > 0:
        #     print(len(data))
        break
    else:
        time.sleep(5)




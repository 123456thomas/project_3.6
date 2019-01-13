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

# 用cookie模拟登录微博
from urllib import request,parse
import chardet,os
# cookie模块
import http.cookiejar

#1.创建headers
headers = {}
headers['Cookie'] = 'login_sid_t=c5ec7c41c11937cbda923f69d5fb28bd; cross_origin_proto=SSL; YF-V5-G0=f59276155f879836eb028d7dcd01d03c; _s_tentry=www.google.com.hk; Apache=8502364359398.411.1547045405269; SINAGLOBAL=8502364359398.411.1547045405269; ULV=1547045405347:1:1:1:8502364359398.411.1547045405269:; Ugrow-G0=169004153682ef91866609488943c77f; wb_view_log=1366*7681; appkey=; un=17625809083; YF-Page-G0=d30fd7265234f674761ebc75febc3a9f; wb_view_log_6368145656=1366*7681; WBStorage=bfb29263adc46711|undefined; UOR=www.google.com.hk,www.weibo.com,login.sina.com.cn; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWu9fAzEy2HI1ZM0E9bWDVY5JpX5K2hUgL.Foq0SonpSh-cSKq2dJLoIEBLxK-L12eL1KqLxKnL1-BLBoqLxK-L1hqLBo5LxKnL1K5LB.Bt; ALF=1578621082; SSOLoginState=1547085083; SCF=Al1wwp4mH7LVty9SL6PXbDttvUG9MhOTvvHrM8TN3M9MaWLp3U9rqJ80UMd3BAz6pTF3U6FDfn9ielBSSUOLP8U.; SUB=_2A25xMtVLDeRhGeBN7VoQ9CvKzjqIHXVSRkGDrDV8PUNbmtBeLUHdkW9NRCq-0SV6tYv9gLh7NMwxxBvDiS6vc6v9; SUHB=0YhRGB6OIr5hOC; wvr=6'
headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'

# 2.定义request对象
Req_url = "https://weibo.com/u/6368145656/home?wvr=5&lf=reg"
req = request.Request(Req_url,headers=headers)

# 3.进行请求，获取响应
response = request.urlopen(req)
html = response.read().decode('utf8','ignore')

# 7.存储响应页面
if not os.path.exists('files'):
    os.mkdir('files')
with open('files/weibo.html','w',encoding='utf8') as f:
    f.write(html)
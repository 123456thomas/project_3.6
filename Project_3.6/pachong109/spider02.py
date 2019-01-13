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

# 获取人人首页使用cookie

from urllib import request,parse
import chardet,os
import http.cookiejar

# 1.创建带cookie的请求头
headers = {}
headers['Cookie'] = 'r01_=1; ick=861462c9-c4b6-4d13-8e76-1f751aa0f06c; anonymid=jqp8m0ii-obbvwu; first_login_flag=1; ln_uact=17752558702; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; depovince=HEN; JSESSIONID=abc5PU6BWZAdx4YtL3YGw; jebe_key=62db5f5a-aeaf-4224-a7cd-771a4ae42cc0%7C077a3e2b1c00096d5c13732ceee74ce5%7C1547041671554%7C1%7C1547041671308; jebe_key=62db5f5a-aeaf-4224-a7cd-771a4ae42cc0%7C077a3e2b1c00096d5c13732ceee74ce5%7C1547041671554%7C1%7C1547041671326; ick_login=29088f18-6bc2-439f-86d6-8bee2ab7a73f; loginfrom=null; wp_fold=0; jebecookies=bb131a09-29f8-4563-82e3-d416095e4a38|||||'
headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'

# 2.定义request对象
Req_url = 'http://www.renren.com/'
req = request.Request(Req_url,headers=headers)

# 3.进行请求，获取响应
response = request.urlopen(req)
html = response.read().decode('utf8','igonre')

# 8.存储响应页面

if not os.path.exists('files'):
    os.mkdir('files')
with open('files/renren.html','w',encoding='utf8') as f:
    f.write(html)
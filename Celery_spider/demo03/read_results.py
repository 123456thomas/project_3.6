"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/10/23'
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

import redis
import json

r = redis.Redis(host='127.0.0.1',password='123',port=6379,db=3)

keys = r.keys()

for key in keys:
    res = r.get(key)
    res = json.loads(res.decode('utf-8'))
    print (res.get('result'))


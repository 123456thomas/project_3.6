"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/10/20'
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
from celery import Celery
uri = 'redis://:123@127.0.0.1:6379/2'
app = Celery('tasks',  backend=uri, broker=uri) #配置好celery的backend和broker

@app.task  #普通函数装饰为 celery task
def add(x, y):
    return x + y



"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/10/8'
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

from selenium import webdriver


driver = webdriver.Chrome()
driver.get ("http://www.youdao.com")
# 向 cookie 中 name 和 value 中添加回话信息,
driver.add_cookie({'name': 'key-aaaaaaa','value': 'value-bbbbb'})
# 遍历 cookie 中 name 和 value 信息并打印对应的信息，并包括添加对应的信息
for cookie in driver.get_cookies():
    print("%s->%s" % (cookie['name'], cookie['value']))
driver.quit ()



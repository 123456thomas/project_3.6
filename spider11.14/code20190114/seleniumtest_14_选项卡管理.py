"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/7/24'
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
import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
time.sleep(3)
browser.execute_script('window.open()')
print(browser.window_handles)
print(type(browser.window_handles[0]))
browser.switch_to_window(browser.window_handles[1])
browser.get('https://www.taobao.com')
time.sleep(3)
browser.switch_to_window(browser.window_handles[0])
browser.get('https://python.org')


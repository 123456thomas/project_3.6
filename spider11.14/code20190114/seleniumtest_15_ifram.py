"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2019/1/13'
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

from selenium import  webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
# get方法会一直等到页面被完全加载，然后才会继续程序，通常测试会在这里选择 time.sleep(2)
driver.get("http://sahitest.com/demo/iframesTest.htm")
time.sleep(2)
print(driver.current_url)
print(driver.page_source)
frames = driver.find_elements_by_tag_name("iframe")
driver.switch_to_frame(frames[0])
print('================================================')
print(driver.page_source)
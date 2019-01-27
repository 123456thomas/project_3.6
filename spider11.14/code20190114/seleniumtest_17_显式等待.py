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
from selenium import webdriver
from selenium.webdriver.common.by import By
# WebDriverWait 库，负责循环等待
from selenium.webdriver.support.ui import WebDriverWait
# expected_conditions 类，负责条件触发
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
try:
    # 页面一直循环，直到 id="myDynamicElement" 出现
    # 智能等待的对象
    wait = WebDriverWait(driver, 10)
    element = wait.until(
        EC.presence_of_element_located((By.ID, "su"))
    )
    print(element.get_attribute('class'))
finally:
    driver.quit()




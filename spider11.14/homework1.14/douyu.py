"""爬取斗鱼直播间名称和人数
https://www.douyu.com/directory/all


"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

# 1.创造driver
baseurl = "https://www.douyu.com/directory/all"
driver = webdriver.Chrome()
driver.get(baseurl)

# 2.元素定位
for i in range(3):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)

lis = driver.find_elements_by_css_selector("#live-list-contentbox > li")
for li in lis:
    title = li.find_element_by_css_selector("li> a > div > div > h3").text
    man_num =li.find_element_by_css_selector("li> a > div > p > span.dy-num.fr").text
    print(title)
    print(man_num)


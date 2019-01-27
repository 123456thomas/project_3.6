
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

import time


urls = "https://www.jd.com/"
# 1.构建自动化测试工具
driver = webdriver.Chrome()
driver.get(urls)
time.sleep(5)

# 2.获得搜索元素
page_source = driver.page_source
input = driver.find_element_by_id("key").send_keys("手机")
button = driver.find_element_by_xpath('//*[@id="search"]/div/div[2]/button')
ActionChains(driver).click(button).perform()
time.sleep(5)
# 如何获取刷新后的页面,driver里为刷新后的页面

for i in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(4)

lis = driver.find_elements_by_class_name("gl-item")
for i in lis:
    title = i.find_element_by_css_selector("div > div.p-name.p-name-type-2 > a > em").text
    price = i.find_element_by_css_selector("div > div.p-price > strong > i").text
    print("title:",title)
    print("price:",price)





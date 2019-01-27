
"""selenium模拟登录豆瓣网
https://www.douban.com/

"""


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# 1.创造driver
baseurl = "https://www.douban.com/"
driver = webdriver.Chrome()
driver.get(baseurl)

# 2.登陆元素定位

account = driver.find_element_by_id("form_email").send_keys("17625809083")
pwd = driver.find_element_by_id("form_password").send_keys("123456")
pwd = driver.find_element_by_id("captcha_field").send_keys("least")

button = driver.find_element_by_css_selector("#lzform > fieldset > div.item.item-submit > input")

# 3.点击提交
ActionChains(driver).click(button).perform()
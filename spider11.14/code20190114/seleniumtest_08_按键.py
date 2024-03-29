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
from selenium.webdriver.common.action_chains import ActionChains
# 要想调用键盘按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys
from time import sleep


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('http://sahitest.com/demo/keypress.htm')

key_up_radio = driver.find_element_by_id('r1')  # 监测按键升起
key_down_radio = driver.find_element_by_id('r2')  # 监测按键按下
key_press_radio = driver.find_element_by_id('r3')  # 监测按键按下升起

enter = driver.find_elements_by_xpath('//form[@name="f1"]/input')[1]  # 输入框
result = driver.find_elements_by_xpath('//form[@name="f1"]/input')[0]  # 监测结果

# 监测key_down
key_down_radio.click()
ActionChains(driver).key_down(Keys.CONTROL, enter).key_up(Keys.CONTROL).perform()
print(result.get_attribute('value'))
sleep(6)
# 监测key_up
key_up_radio.click()
enter.click()
ActionChains(driver).key_down(Keys.SHIFT).key_up(Keys.SHIFT).perform()
print(result.get_attribute('value'))
sleep(6)
# 监测key_press
key_press_radio.click()
enter.click()
ActionChains(driver).send_keys('a').perform()
print(result.get_attribute('value'))
sleep(6)
driver.quit()







from selenium import webdriver
import time, random
from selenium.webdriver.common.action_chains import ActionChains

# 1.创建driver
driver = webdriver.Chrome()

driver.get("https://www.marriott.com/")
action = ActionChains(driver)
# 延时设置，确保网页刷新
time.sleep(5)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
print(driver.page_source)
while True:
    try:
        address = driver.find_element_by_xpath()
        action.move_to_element(address)
        address.send_keys("shanghai")
        button1 = driver.find_element_by_xpath('//*[@id="find-a-hotel-homePage-form"]/div[2]/div[4]/button')
        button1.click()
        break
    except:
        time.sleep(2)
        print("1111223")

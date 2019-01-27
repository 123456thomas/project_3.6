
from selenium import webdriver
import time,re

# 1.创建driver
driver = webdriver.Chrome()

driver.get("http://tech.163.com/")
# 延时设置，确保网页刷新
time.sleep(5)
heigh0 = driver.execute_script("return document.body.scrollHeight")
print("height:",heigh0)
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    heigh1 = driver.execute_script("return document.body.scrollHeight")
    print("height:", heigh0)
    if heigh0 == heigh1:
        break
    heigh0 = heigh1
pattern = re.compile(r"")
lis = driver.find_elements_by_xpath('//li[@class="newsdata_item"]/div[@class="ndi_main"]/div[contains(@class,"data_row ")]')
print(len(lis))
yishi = []
for s in range(0,len(lis)):
    try:
        href = lis[s].find_element_by_css_selector('h3>a').get_attribute('href')
        title = lis[s].find_element_by_css_selector('h3>a').text
        print("title",title)
        print("href",href)
    except:
        yishi.append(s)
        continue
print(yishi)
# driver.switch_to_window(driver.window_handles[0])
# driver.back()
driver.close()

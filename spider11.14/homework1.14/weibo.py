
from selenium import webdriver
import time

# 1.创建driver
driver = webdriver.Chrome()

driver.get("https://www.weibo.com/")
# 延时设置，确保网页刷新
time.sleep(5)

# 2.模拟登陆
users = driver.find_element_by_id("loginname").send_keys('17625809083')
pwd = driver.find_element_by_name("password").send_keys('********')
button = driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a')
button.click()
time.sleep(5)
# 3.模拟输入，进行页面跳转
while True:
    try:
        search = driver.find_element_by_css_selector("#plc_top > div > div > div.gn_search_v2 > input").send_keys('王思聪')
        button2 = driver.find_element_by_xpath('//*[@id="plc_top"]/div/div/div[2]/a')
        break
    except:
        time.sleep(2)
button2.click()
time.sleep(2)
# 4.页面跳转
while True:
    try:
        button3 = driver.find_element_by_xpath('//*[@id="pl_feedlist_index"]/div[1]/div[1]/div/div[2]/div/a[1]')
        break
    except:
        time.sleep(2)
        pass
button3.click()
time.sleep(3)
# 5.信息榨取
driver.switch_to_window(driver.window_handles[1])
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

time.sleep(5)
lis = driver.find_elements_by_xpath('//*[@id="Pl_Official_MyProfileFeed__20"]/div/div')
print(len(lis))
for s in range(1,len(lis)):
    dattime = lis[s].find_element_by_css_selector('.WB_feed_detail.clearfix > div.WB_detail > div.WB_from.S_txt2 > a').text
    texts = lis[s].find_element_by_css_selector('.WB_feed_detail.clearfix > div.WB_detail > div.WB_text.W_f14').text
    zhuanfa = lis[s].find_element_by_css_selector('.WB_feed_handle > div > ul > li:nth-child(2) > a > span > span > span > em:nth-child(2)').text
    talk = lis[s].find_element_by_css_selector('.WB_feed_handle > div > ul > li:nth-child(3) > a > span > span > span > em:nth-child(2)').text
    zan = lis[s].find_element_by_css_selector('.WB_feed_handle > div > ul > li:nth-child(4) > a > span > span > span > em:nth-child(2)').text
    print("dattime",dattime)
    print("texts",texts)
    print("zhuanfa",zhuanfa)
    print("talk",talk)
    print("zan",zan)

driver.switch_to_window(driver.window_handles[0])
driver.back()

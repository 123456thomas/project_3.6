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

# 导入 webdriver自动化测试工具
from selenium import webdriver
# 要想调用键盘按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys
import time

# 调用环境变量指定的PhantomJS浏览器创建浏览器对象
#driver = webdriver.PhantomJS()
driver = webdriver.Chrome()

# get方法会一直等到页面被完全加载，然后才会继续程序，通常测试会在这里选择 time.sleep(2)
driver.get("http://www.baidu.com/")
print(driver.page_source)
time.sleep(2)
driver.execute_script("return document.body.scrollHeight")
# 获取页面名为 wrapper的id标签的文本内容
data = driver.find_element_by_id("wrapper").text

# 打印数据内容
print(data)
#打印页面标题 "百度一下，你就知道"
print(driver.title)
# 生成当前页面快照并保存
driver.save_screenshot("./images/baidu.png")

# id="kw"是百度搜索输入框，输入字符串"长城"
driver.find_element_by_id("kw").send_keys("奇酷信息")

# id="su"是百度搜索按钮，click() 是模拟点击
driver.find_element_by_id("su").click()
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# 获取新的页面快照
driver.save_screenshot("./images/qiku.png")

# 打印网页渲染后的源代码
print(driver.page_source)
print('============')
# 获取当前页面Cookie
print(driver.get_cookies())
time.sleep(2)
# 清除输入框内容
driver.find_element_by_id("kw").clear()
print('============')
# 获取当前url
print(driver.current_url)
time.sleep(2)
# 关闭当前页面，如果只有一个页面，会关闭浏览器
driver.close()

# 关闭浏览器
driver.quit()

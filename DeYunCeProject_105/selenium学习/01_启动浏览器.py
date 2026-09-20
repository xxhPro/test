from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time


s = Service("chromedriver.exe")

driver = webdriver.Chrome(service = s)

driver.maximize_window()

driver.get("https://www.baidu.com/")

time.sleep(3)
# 关闭浏览器
driver.quit()    # close关闭一个页面   quite是关闭浏览器

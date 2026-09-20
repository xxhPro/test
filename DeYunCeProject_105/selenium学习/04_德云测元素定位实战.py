from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By


s = Service("chromedriver.exe")
driver = webdriver.Chrome(service = s)

driver.maximize_window()

driver.get("http://wall.deyunce.com/")

time.sleep(3)

# ================新内容====================
driver.find_element(By.ID,"nameInput").send_keys("德云测")
time.sleep(3)


# 关闭浏览器
driver.quit()    # close关闭一个页面   quite是关闭浏览器

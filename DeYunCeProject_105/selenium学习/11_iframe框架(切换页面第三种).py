from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By


s = Service("chromedriver.exe")
driver = webdriver.Chrome(service = s)

driver.maximize_window()

driver.get("http://wall.deyunce.com/")
time.sleep(1)

# ================新内容====================

driver.find_element(By.XPATH,'//button[@id="drawOneBtn"]').click()
time.sleep(2)


# 切换到alert弹窗
driver.switch_to.alert.accept()
time.sleep(2)
# accept()   代表点击确定
# dismiss()  代表点击取消
# send_keys()  代表输入


# 点击砸彩蛋
driver.find_element(By.XPATH, "//button[text()='砸彩蛋']").click()
time.sleep(3)

ifr = driver.find_element(By.ID,"iframe-container")
driver.switch_to.frame(ifr)
time.sleep(3)

driver.find_element(By.XPATH,'//button[@class="close-btn"]').click()
time.sleep(3)

# 关闭浏览器
driver.quit()    # close关闭一个页面   quite是关闭浏览器

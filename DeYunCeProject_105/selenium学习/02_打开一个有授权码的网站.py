from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time


s = Service("chromedriver.exe")

driver = webdriver.Chrome(service = s)

driver.maximize_window()

# 打开一个网址
# 授权码写在 http 后面 域名前面  使用用户名：密码 @ 域名
driver.get("https://deyunce:210511@mall.deyunce.com")

time.sleep(3)
# 关闭浏览器
driver.quit()    # close关闭一个页面   quite是关闭浏览器

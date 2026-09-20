"""
1.打开商城，注意授权码
2.点击登录
3.点击账号密码登录（注意不要点击 不然属性变化 使用class属性）
4.输入账号、输入密码
5.点击登录（定位多个元素，下标1 click）
6.获取昵称（使用class属性）

"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By


s = Service("chromedriver.exe")
driver = webdriver.Chrome(service = s)

driver.maximize_window()

# 打开一个网址
# 授权码写在 http 后面 域名前面  使用用户名：密码 @ 域名
driver.get("https://deyunce:210511@mall.deyunce.com")
time.sleep(3)

driver.find_element(By.XPATH,'//a[@href="/pc/account/login"]').click()
time.sleep(3)

driver.find_element(By.XPATH,'//div[@class="header-tab xxl"]').click()
time.sleep(3)

driver.find_element(By.XPATH,'//input[@placeholder="请输入账号/手机号码"]').send_keys("13657985592")
driver.find_element(By.XPATH,'//input[@placeholder="请输入密码"]').send_keys("hqn789")
time.sleep(1)

an = driver.find_elements(By.XPATH,'//button[@type="button"]')
an[2].click()
time.sleep(1)

nm = driver.find_element(By.XPATH,'//a[@class="el-popover__reference"]')
print(nm.text)

time.sleep(2)
# 关闭浏览器
driver.quit()    # close关闭一个页面   quite是关闭浏览器


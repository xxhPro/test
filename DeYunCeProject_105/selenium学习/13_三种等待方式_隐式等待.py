
# ！！！ 面试只要提到ui自动化  经常会问的问题
# 等待页面元素出现
# 第一种：强制等待   time.sleep   设置多久就等多久

# 第二种：隐式等待   全局的，只需要设置一次  设置之后找所有都会自动等待
# 找到元素出现之后  可以直接继续执行后续代码  不需要把时间消耗完
# 如果找不到元素  就继续等待  最多等到设置的时间  如果还是找不到 报错
# driver.implicitly_wait(10)

import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("chromedriver.exe")
driver = Chrome(service=s)
driver.maximize_window()
driver.implicitly_wait(10)

# 打开商城
driver.get("https://deyunce:210511@mall.deyunce.com/")
driver.find_element(By.XPATH,'//input[@placeholder="请输入商品名称"]').send_keys("黄金")

time.sleep(3)
driver.quit()


# 隐式等待是全局的  针对页面上所有元素起作用
# 设置了之后  只要找不到都会等待

# 显式等待   （智能等待）  针对某一个特定元素 特定状态等待
# 元素状态：显示、不显示、可点击、不可点击

# 显式等待 用起来有点复杂，了解即可
# 1.导入等待器   WebDriverWait
# 2.导入等待条件 expected_conditions

import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions  as ec
from selenium.webdriver.support.wait import WebDriverWait

s = Service("chromedriver.exe")
driver = Chrome(service=s)
driver.maximize_window()
driver.get("https://deyunce:210511@mall.deyunce.com/")

# WebDriverWait
# expected_conditions

wait = WebDriverWait(driver,10,0.5)
ssk = wait.until(ec.visibility_of_element_located((By.XPATH,'//input[@placeholder="请输入要搜索的商品名称"]')))
ssk.send_keys("斯文")

time.sleep(10)
driver.quit()


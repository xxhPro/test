
# 八种定位方式
#    *** 重点：ID、XPATH ***
# 其他的了解即可，看过就行：name、class、link_text、partial_link_text、tag、css


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
# ===================通过 name 进行定位====================
# driver.find_element(By.NAME,"nameInput").send_keys("德云测")
# time.sleep(2)


# ===================通过 name 进行定位====================
# driver.find_element(By.CLASS_NAME,"control-btn").click()
# time.sleep(5)


# --------------超链接文本定位    极其没用，因为只能a标签--------------
# driver.find_element(By.LINK_TEXT, "德德").click()  # 文本要完全一致，不能多不能少
# time.sleep(5)

# driver.find_element(By.PARTIAL_LINK_TEXT, "云").click()  # 包含文本就可以
# time.sleep(5)


# --------------tag 标签名称定位  也很没用，除非只有一个这个标签--------------

driver.find_element(By.TAG_NAME, "input").send_keys("标签名称定位")
time.sleep(5)


# 关闭浏览器
driver.quit()    # close关闭一个页面   quite是关闭浏览器


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By


s = Service("chromedriver.exe")

driver = webdriver.Chrome(service = s)

driver.maximize_window()

# 打开一个网址
# 授权码写在 http 后面 域名前面  使用用户名：密码 @ 域名
driver.get("https://www.baidu.com")
time.sleep(1)

# ==============新知识区域==================
# 定位包含【新闻】的元素 点击    # //标签名称[text()="文字"]
driver.find_element(By.XPATH, '//span[text()="张一鸣成亚洲首富"]').click()
time.sleep(3)

# 包含文字      //标签名称[contains(text(),"文字")]
driver.find_element(By.XPATH,'//a[contains(text(),"新闻")]').click()
time.sleep(3)

# 截图
driver.save_screenshot("百度截图.png")

# 关闭浏览器
driver.quit()    # close关闭一个页面   quite是关闭浏览器


# 代码点击之后，可能会打开新页面，但是默认情况下，代码操作还是在原来的页面
# 所以直接查找新页面的元素，是找不到的，需要切换到新页面才可以

# 定位新打开的百度新闻输入框


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

# 获取全部页面
xin = driver.window_handles[-1]
driver.switch_to.window(xin)
time.sleep(3)

# 定位新打开的百度输入框
driver.find_element(By.ID,'ww').send_keys("德云测")
time.sleep(3)
# 截图
# driver.save_screenshot("百度截图.png")

# 关闭浏览器
driver.quit()    # close关闭一个页面   quite是关闭浏览器

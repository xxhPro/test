
# driver.find_element      代表查找单个元素，如果多个，给你第一个出现的
# 获取搜索结果  find_element   只能获取结果里面的第一个
# driver.find_elements     代表查找多个元素，把能够找到的所有元素都给你

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
time.sleep(5)

# 搜索
ssk = driver.find_element(By.XPATH, '//input[@placeholder="请输入要搜索的商品名称"]')
ssk.send_keys("德云测")

# 点击
driver.find_element(By.XPATH,'//div[@class="search-btn bg-primary white row-center"]').click()
time.sleep(4)

# 获取商品的文本信息
# tx = driver.find_element(By.XPATH,'//div[@class="name line2"]').text
# print(tx)

tx = driver.find_elements(By.XPATH,'//div[@class="name line2"]')
print(type(tx))

# for t in tx:
#     print(t.text)

# 获取搜索结果的第二个商品的名称
print(tx[1].text)

time.sleep(3)


# 关闭浏览器
driver.quit()    # close关闭一个页面   quite是关闭浏览器

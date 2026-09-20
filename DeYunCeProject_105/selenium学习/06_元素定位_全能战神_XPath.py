
# 之前讲了很多定位方式，但是都不实用，每种都有自己的局限，只能使用某个属性
# xpath 可以使用【任何】属性, 在实际使用中用的最多

# 有自己特定的编写格式，不能乱写

# xpath语法
# 直接可以定位到元素：  //标签名[@属性名称=属性值]
# 不能直接定位的：    //标签名[@属性名称=属性值]/标签名[@属性名称=属性值]

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
time.sleep(1)

ssk = driver.find_element(By.XPATH, '//input[@placeholder="请输入要搜索的商品名称"]')
ssk.send_keys("德云测")

driver.find_element(By.XPATH,'//div[@class="search-btn bg-primary white row-center"]').click()

time.sleep(3)

# 关闭浏览器
driver.quit()    # close关闭一个页面   quite是关闭浏览器

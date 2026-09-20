import requests


url = "https://img2.baidu.com/it/u=851"


# 发送请求
res = requests.get(url=url)
print(res.status_code)
# print(res.text)


ejz = res.content # 字节---二进制


# 把原始的二进制的信息  写到文件里面
f = open("atm.png","wb")  # 打开一个文件
f.write(ejz) # 写入奥特曼图片的内容


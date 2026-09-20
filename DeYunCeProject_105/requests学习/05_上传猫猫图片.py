import requests

# 四大金刚
# 请求方式
method = "post"

# 请求路径
url = "https://api.thecatapi.com/v1/images/upload"


# 请求头
headers = {
    "x-api-key": "live_YNpuCsDshHUEW0aAFwLvMezjcWzAhus6ZDcLp0d13s2ZaLWM1FX9Su5Rs8bW0ivB"
}


# 请求体  文件类型的内容
files = {
    "file":("g.png",open("g.png","rb"),"image/png")
    # 元组里面的内容（文件名字,文件的二进制数据,文件类型）
}


# 发送请求
res = requests.post(url=url,headers=headers,files=files)
print(res.status_code)
print(res.json())
# print(res.text)

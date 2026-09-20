from http.client import responses

import requests

# 登录接口的四大金刚
# 请求方式
method = "get"

# 请求路径（地址）
url = "https://mall.deyunce.com/api/cart/lists"

# 请求头
headers = {
    "authorization": "Basic ZGV5dW5jZToyMTA1MTE=",
    "content-type": "application/json",
    "token": "5f3d326150a4a04519b992b34a059167"
}

# 请求体
# body = {
#     "account": "13657985592",
#     "password": "hqn789",
#     "client": 5
# }


res = requests.get(url = url, headers = headers)
# print(response)

print(res.status_code)  # 状态码
print(res.json())  # json格式的响应体  ✅通常使用    可以根据键值对取值
# print(response.text)    # 文本格式的响应体    这个是通用，不会报错的方式    这个不可以键值对取值

# 获取购物车里面的第一个商品的名字
r = res.json()
data = r["data"]
print(data)

lst = data["lists"]
print(lst)

sp1 = lst[0]
print(sp1)

print(sp1["name"])
print(r["data"]["lists"][0]["name"])





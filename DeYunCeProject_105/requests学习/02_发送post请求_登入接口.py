from http.client import responses

import requests

# 登录接口的四大金刚
# 请求方式
method = "get"

# 请求路径（地址）
url = "https://mall.deyunce.com/api/account/login"

# 请求头
headers = {
    "authorization": "Basic ZGV5dW5jZToyMTA1MTE=",
    "content-type": "application/json"
}

# 请求体
body = {
    "account": "13657985592",
    "password": "hqn789",
    "client": 5
}


# Response 是这个 class 创建出来的对象。
response = requests.post(url = url, headers = headers, json = body)
# print(response)

print(response.status_code)  # 状态码
print(response.json())  # json格式的响应体  ✅通常使用    可以根据键值对取值
# print(response.text)    # 文本格式的响应体    这个是通用，不会报错的方式    这个不可以键值对取值

# 提取 msg   $.msg
# 提取 token   $.data.token

r = response.json()
print(type(r))

print(r["msg"])
print(r["data"]["token"])

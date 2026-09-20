import requests

# 四大金刚提前准备
# 请求的路径 （完整的接口地址）
url = 'https://mall.deyunce.com/api/account/login'
# 请求方式
method = "post"
# 请求头
headers = {
    "authorization": "Basic ZGV5dW5jZToyMTA1MTE=",
    "content-type": "application/json",
}
# 请求体
body = {
    "account": "13657985592",
    "password": "hqn789",
    "client": 5
}

# 发送post请求
# requests.post(三大金刚)
# requests.get(三大金刚)

# 发送登录请求
response = requests.post(url = url,headers = headers,json = body)  # 表单data参数  # get请求有params
# print(response)   # <Response [200]>  这个太不详细了

# 获取响应状态码
print(response.status_code)

# 获取响应体内容
print(response.json())   # json格式的响应的时候使用这个
# 文本格式   json报错的时候 用这个
print(response.text)

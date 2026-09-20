import random
import requests

# 注册接口
def test_register():
    method = "post"  # 请求方式
    url = "https://mall.deyunce.com/api/account/register"  # 接口地址
    headers = {  # 头信息
        "content-type": "application/json",
        "authorization": "Basic ZGV5dW5jZToyMTA1MTE="
    }

    sjh = str(random.randint(130_0000_0000, 199_9999_9999))
    body = {
        "mobile": sjh,
        "password": "a123456",
        "code": "",
        "client": 5
    }

    # 发送请求
    res = requests.request(method = method, url = url, headers = headers, json = body)

    ztm = res.status_code  # 状态码
    res_json = res.json()
    print(f"手机号{sjh},状态码是 {ztm},响应信息是 {res_json}")

    # assert  是用来做断言的
    # assert  预期结果 == 实际结果

    msg = res_json["msg"]

    assert 200 == ztm
    assert "注册成功" == msg


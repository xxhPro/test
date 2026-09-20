
import requests

# 1.先进行登录、
# 2.之后从登录里面拿到token
# 3.调用钱包接口（头信息里面传递提取的token）
# 4.断言----它的响应状态码是 200


def login_wallet():
    print("==========准备进行登录接口的请求===========")
    method_login = "post"

    url_login = "https://mall.deyunce.com/api/account/login"

    headers_login = {
        "authorization": "Basic ZGV5dW5jZToyMTA1MTE=",
        "content-type": "application/json",
    }

    body_login = {
        "account": "13657985592",
        "password": "hqn789",
        "client": 5
    }

    res = requests.request(method = method_login,
                           url = url_login, headers = headers_login,
                           json = body_login)

    print(f"登录接口的响应状态码：{res.status_code}")
    res_json = res.json()
    print(f"登录接口的响应信息：{res_json}")

    t = res_json["data"]["token"]
    print(f"从登录接口中提取到的token：{t}")

    print("===============登录已经完成，拿到token信息了 下面开始查询余额=================")
    url_yue = "https://mall.deyunce.com/api/user/myWallet"

    method_yue = "get"

    headers_yue = {
        "authorization": "Basic ZGV5dW5jZToyMTA1MTE=",
        "content-type": "application/json",
        "token": t
    }

    cs_yue = {
        "page_size": 10,
        "page_no": 1,
        "type": 0,
        "source": 1
    }

    res_yue = requests.request(url = url_yue, method = method_yue,
                               headers = headers_yue, params = cs_yue)

    print("余额接口的响应状态码", res_yue.status_code)
    print("余额接口的响应信息", res_yue.json())


login_wallet()

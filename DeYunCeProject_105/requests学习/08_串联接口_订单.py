
import requests

def ding_dan(t):
    url = "https://mall.deyunce.com/api/order/lists"
    method = "get"
    headers = {
        "authorization": "Basic ZGV5dW5jZToyMTA1MTE=",
        "content-type": "application/json",
        "token": t
    }

    can_shu = {
        "page_size": 10
    }

    res = requests.get(url = url, headers = headers, params = can_shu)
    print(res.status_code)
    print(res.json())


ding_dan("ec7ec99b3e0d1ac23a3db23a689fee01")


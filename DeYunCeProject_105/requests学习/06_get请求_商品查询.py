import requests
from Tools.scripts.generate_opcode_h import header

method = "get"

url = "https://mall.deyunce.com/api/pc/goodsList"

headers = {
    "authorization": "Basic ZGV5dW5jZToyMTA1MTE=",
    "content-type": "application/json",
    "token": "5f3d326150a4a04519b992b34a059167"
}

can_shu = {
    "page_size": "20",
    "name": "余杰"
}

res = requests.request(method = method, url = url, headers = headers, params = can_shu)
print(res.status_code)
print(res.json())


import requests

headers = {"user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWe bKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}
post_data = {
    "query":" 人生苦短，我用python",
    "from": "zh",
    "to": "en",
    "token":" 2ad85843902c57f82c2bed5083b83e14",
    "sign": "289133.35420"
    }
post_url = "https://fanyi.baidu.com/extendtrans"


r = requests.post(post_url,headers = headers,data = post_data)
print(r.content.decode())






import requests
import json
import sys

query_string = sys.argv[1]    #写什么翻译什么

headers = {"user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWe bKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}
post_data = {
    #"query":" 人生苦短，我用python",
"query":query_string,
"from": "zh",
"to": "en",
"token":" 2ad85843902c57f82c2bed5083b83e14",
"sign": "289133.35420"
    }
post_url = "https://fanyi.baidu.com/extendtrans"


r = requests.post(post_url,headers = headers,data = post_data)
print(r.content.decode())

dict_ret = json.loads(r,content.decode())
ret = dict_ret["trans"][0]["dst"]
print("result is :",ret)

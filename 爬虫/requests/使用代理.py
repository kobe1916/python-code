#代理 用法  requests.get("http://www.baidu.com",proxies = proxies)
# proxies的形式：字典
'''
proxies = {
    "http":"http://12.34.56.79:9527",
    "http":"http://12.34.56.79；9527”，
    }
    '''
import requests


proxies = {"http":"http://163.177.151.23:80"}
headers = {"user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWe bKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}

r = requests.get("http://www.baidu.comm",proxies = proxies,headers = headers)
print(r.status_code)
    

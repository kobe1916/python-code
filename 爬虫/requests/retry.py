import requests
from retrying import retry

headers ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}

@retry(stop_max_attempt_number = 3)  #装饰器
def _parse_url(url):
    print("*"*20)
    res = requests.get(url,headers = headers,timeout = 3)
    assert res.status_code ==200
    return res.content.decode()

def parse_url(url):
    try:
        html_str = _parse_url(url)
    except:
        hrml_str = None

    return html_str

if __name__ == '__main__':
    url = "http://www.baidu.com"
    print(parse_url(url))




'''
import requests
from retrying import retry

headers ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
@retry(stop_max_attempt_number = 3)  #装饰器
def _parse_url(url,method,data):
    print("*"*20)
    if method =="POST":
        res = requests.get(url,data = data,headers = headers,timeout = 3)
    else:
        res = requests.get(url,headers = headers,timeout = 3)
    assert res.status_code ==200
    return res.content.decode()

def parse_url(url,method = "GET",data = None):
    try:
        html_str = _parse_url(url,method,data)
    except:
        hrml_str = None

    return html_str

if __name__ == '__main__':
    url = "http://www.baidu.com"
    print(parse_url(url))
'''

import requests
from retrying import retry

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

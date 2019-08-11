In [1]: import requests

In [2]: response = requests.get("http://www.baidu.com")

In [3]: response.cookies
Out[3]: <RequestsCookieJar[Cookie(version=0, name='BDORZ', value='27315', port=None, port_specified=False, domain='.baidu.com', domain_specified=True, domain_initial_dot=True, path='/', path_specified=True, secure=False, expires=1565444418, discard=False, comment=None, comment_url=None, rest={}, rfc2109=False)]>

In [4]: requests.utils.dict_from_cookiejar(response.cookies)
Out[4]: {'BDORZ': '27315'}

In [5]: requests.utils.cookiejar_from_dict(response.cookies)
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-5-b03cd05314c5> in <module>
----> 1 requests.utils.cookiejar_from_dict(response.cookies)

c:\users\lhy\appdata\local\programs\python\python37\lib\site-packages\requests\cookies.py in cookiejar_from_dict(cookie_dict, cookiejar, overwrite)
    522         for name in cookie_dict:
    523             if overwrite or (name not in names_from_jar):
--> 524                 cookiejar.set_cookie(create_cookie(name, cookie_dict[name]))
    525
    526     return cookiejar

c:\users\lhy\appdata\local\programs\python\python37\lib\site-packages\requests\cookies.py in __getitem__(self, name)
    326         .. warning:: operation is O(n), not O(1).
    327         """
--> 328         return self._find_no_duplicates(name)
    329
    330     def __setitem__(self, name, value):

c:\users\lhy\appdata\local\programs\python\python37\lib\site-packages\requests\cookies.py in _find_no_duplicates(self, name, domain, path)
    397         if toReturn:
    398             return toReturn
--> 399         raise KeyError('name=%r, domain=%r, path=%r' % (name, domain, path))
    400
    401     def __getstate__(self):

KeyError: "name=Cookie(version=0, name='BDORZ', value='27315', port=None, port_specified=False, domain='.baidu.com', domain_specified=True, domain_initial_dot=True, path='/', path_specified=True, secure=False, expires=1565444418, discard=False, comment=None, comment_url=None, rest={}, rfc2109=False), domain=None, path=None"

In [6]: requests.utils.quote("http://www.baidu.com")
Out[6]: 'http%3A//www.baidu.com'

In [7]: requests.utils.unquote( 'http%3A//www.baidu.com')
Out[7]: 'http://www.baidu.com'

#SSL证书验证 get(url,verify=False)
In [10]: requests.get("https://www.12306.cn/mormhweb/")
Out[10]: <Response [200]>

In [11]: requests.get("https://www.12306.cn/mormhweb/",verify=False)
c:\users\lhy\appdata\local\programs\python\python37\lib\site-packages\urllib3\connectionpool.py:851: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
  InsecureRequestWarning)
c:\users\lhy\appdata\local\programs\python\python37\lib\site-packages\urllib3\connectionpool.py:851: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
  InsecureRequestWarning)
Out[11]: <Response [200]>

#设置超时
r = requests.get(url,timeout = 10)

#配合状态码判断请求是否成功assert r.status_code ==200

import requests


session = requests.session()
post_url = "https://user.qzone.qq.com/604368100/infocenter"
post_data = {"qq":"604368100","passwors":"Fighting.2017"}

headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}

session.post(post_url,data = post_data,headers = headers)
r = session.get("https://user.qzone.qq.com/604368100/infocenter",headers=headers)

with open("qq.html","w",encoding = "utf-8") as f:
    f.write(r.content.decode())

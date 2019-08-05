import requests

#发送请求
r = requests.get("https://www.baidu.com/img/bd_logo1.png?where=super")

#保存
with open("a.png","wb") as f:
    f.write(r.content)
    

import requests

#发送请求
r = requests.get("https://www.baidu.com/img/bd_logo1.png?where=super")

#保存
#根据文件的类型写后缀    a.png   eg: jpg  mp3/4  pdf...
with open("a.png","wb") as f:
    f.write(r.content)
    

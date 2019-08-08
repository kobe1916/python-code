import requests


headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
           "cookie": "604368100_todaycount=0; 604368100_totalcount=53462; RK=QVAduY2QO+; ptcz=e294a8e4175f0fd75b198bee16a497f39085fbcc3d165b518cf638f8d30e6762; pgv_pvid=6416086125; QZ_FE_WEBP_SUPPORT=1; pgv_pvi=8721037312; tvfe_boss_uuid=d175e250452fa203; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221693e6f780b238-0af64e96535308-b781636-1327104-1693e6f780c9%22%2C%22%24device_id%22%3A%221693e6f780b238-0af64e96535308-b781636-1327104-1693e6f780c9%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fcn.bing.com%2F%22%2C%22%24latest_referrer_host%22%3A%22cn.bing.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%7D; eas_sid=l105W5t5z7D3r8s9H6y6P0J7J0; ied_qq=o0604368100; __Q_w_s_hat_seed=1; qz_screen=1536x864; ptui_loginuin=604368100; cpu_performance_v8=1; __Q_w_s__QZN_TodoMsgCnt=1; o_cookie=2974064358; uin=o0604368100; skey=@sa7Rxdm7a; ptisp=ctc; p_uin=o0604368100; pt4_token=Debczx62AWjaUyEHDHb-cP8i1XjKClamk*-CVR9Bu3E_; p_skey=N6TaoDmsyVk1kyy-G795qwNkIEOpRxOEyaFfU*OrymI_; Loading=Yes; pgv_info=ssid=s7384330594"}


//人人网   登陆网址  form表单中action
r = requests.get("https://user.qzone.qq.com/604368100/infocenter",headers = headers)

with open("qq2.html","w",encoding = "utf-8") as f:
    f.write(r.content.decode())


'''
字典推导式
字典是无序的
In [4]: {i:i+10 for i in range(10)}
Out[4]: {0: 10, 1: 11, 2: 12, 3: 13, 4: 14, 5: 15, 6: 16, 7: 17, 8: 18, 9: 19}

In [5]: {i:"b" for i in range(10)}
Out[5]:
{0: 'b',
 1: 'b',
 2: 'b',
 3: 'b',
 4: 'b',
 5: 'b',
 6: 'b',
 7: 'b',
 8: 'b',
 9: 'b'}
 '''

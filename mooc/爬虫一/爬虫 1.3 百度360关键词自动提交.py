#360 ：  q = 关键词
#百度 ：  wd = 关键词
import requests
try:
    kv = {'wd':'python'}
    url = 'http://www.baidu.com/s'
    r = requests.get(url,params=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.request.url)
    print(len(r.text))
except:
    print('爬取失败')
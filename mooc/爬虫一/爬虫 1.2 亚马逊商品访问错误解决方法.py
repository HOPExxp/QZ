# import requests
# url = 'https://www.amazon.cn/gp/product/B01M8L5Z3Y'
# r = requests.get(url)
# r.raise_for_status()
# r.encoding = r.apparent_encoding
# print(r.status_code)
# print(r.request.headers)
# print(r.text[1000:1500])


import requests
url = 'https://www.amazon.cn/gp/product/B01M8L5Z3Y'
try:
    r = requests.get(url)
    r.raise_for_status()
    # print(r.status_code)
    r.encoding = r.apparent_encoding
    print(r.status_code)
    print(r.request.headers)
    print(r.text[1000:1500])
except:
    print('爬取失败')
#
import requests
url = 'https://www.amazon.cn/gp/product/B01M8L5Z3Y'
try:
    header = {'user-agent':'mozilla/5.0'}
    r = requests.get(url,headers = header)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.status_code)
    print(r.text[1000:1500])
except:
    print('爬取失败')

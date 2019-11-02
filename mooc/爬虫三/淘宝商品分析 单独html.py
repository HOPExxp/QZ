import requests
import re
from bs4_test import BeautifulSoup
# def gethtmltext(url):
#     try:
#         r=requests.get(url,timeout=30)
#         r.raise_for_status()
#         # print(r.status_code)
#         r.encoding =r.apparent_encoding
#         return r.text
#     except:
#         print("1")
#
# url='https://s.taobao.com/search?q=书包&s=0'
# html = gethtmltext(url)
# # print(html[:200])
# pattern = re.compile(r'price')
# print(type(pattern))
# ili = pattern.findall(html)
# print(ili)

kv = {'user-agent':'mozilla/5.0'}
url1 = 'http://s.taobao.com/search?q=%E8%83%8C%E5%8C%85'
r1 = requests.get(url1, headers=kv)
html1 = r1.text
soup1 = BeautifulSoup(html1, 'html.parser')
contents = soup1.find('div',id = 'mainsrp-itemlist').find_all('div')
# contents = soup1.find_all('div', class_='ctx-box J_MouseEneterLeave J_IconMoreNew')
print(len(contents))
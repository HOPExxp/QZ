from pyquery import PyQuery as pq
import requests

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 ' \
     '(KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

url = 'https://www.51shucheng.net/wangluo/'

r = requests.get(url,headers = headers)
print(r)
r.encoding = 'utf-8'
html = r.text
# print(html)

doc = pq(html)
# print(doc)
data = doc('li.cat-item a')
# for i,j in enumerate(data.items()):
#     print(i,j.attr('href'))

# 第一本书的url
shu = data.attr('href')
print(shu)

# 获取html
r1 = requests.get(shu,headers = headers)
# print(r1)
r1.encoding = 'utf-8'
html1 = r1.text
# print(html1[:100])


doc1 = pq(html1)
data1 = doc1('div.mulu-list ul li a')
# for j in data1.items():
#     print(j.text())

# 第一本书的第一章的url
shu1 = data1.attr('href')
# print(shu1)

# 获取html
r2 = requests.get(shu1,headers = headers)
r2.encoding = 'utf-8'
html2 = r2.text
# print(html2[:100])

doc2 = pq(html2)
data2 = doc2('h1')
print(data2)
data3 = doc2('div.neirong p')
print(data3.text())
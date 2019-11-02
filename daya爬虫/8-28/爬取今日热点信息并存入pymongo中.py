import requests
from bs4 import BeautifulSoup
import re
import pymongo
from time import sleep

url = 'http://top.baidu.com/buzz?b=341&c=513&fr=topbuzz_b341_c513'

header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                 '(KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

r = requests.get(url = url, headers = header)
r.raise_for_status()
r.encoding = r.apparent_encoding
html = r.text
# print(html[:100])

soup = BeautifulSoup(html,'html.parser')
# print(soup)

# res1 = soup.find_all('td',class_='first')
# # print(res1)
# res2 = soup.find_all('td',class_ = 'keyword')
#
# res3 = soup.find_all('td',class_ = 'tc')
#
# res4 = soup.find_all('td',class_ = 'last')

# for a,b,c,d in zip(res1,res2,res3,res4):
#     print(a)
#     print(b)
#     print(c)
#     print(d)

client = pymongo.MongoClient(host='localhost',port=27017)
# db = client.text
# collection = db.baidu_today_hot
db = client.baidu
# collection = db.todayhot  错误数据
collection = db.todayhot1

for data in soup.find_all('tr'):
    # for i in data.find_all('span',class_ = re.compile('num-')):
    #     print(i.get_text())
    # for i in data.find_all('a',class_ = 'list-title'):
    #     print(i.get_text())
    # for i in data.find_all('span',class_ = 'icon-rise'):
    #     print(i.get_text())

    # for i in data.find_all('span',class_ = re.compile('icon-(rise)|(fall)')):
    #     print(i)

    item0 = data.find_all('span',class_ = re.compile('num-'))
    item1 = data.find_all('a',class_ = 'list-title')
    # item2 = data.find_all('span',class_ = 'icon-rise')
    item2 = data.find_all('span',class_ = re.compile('icon-(rise)|(fall)'))
    for i,j,k in zip(item0,item1,item2):
        data = {
            'index':i.get_text(),
            'describe':j.get_text(),
            'hotpoint':k.get_text()
        }
        print(data)
        collection.insert_one(data)
        sleep(1)



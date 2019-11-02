import requests
from time import sleep
import re
from pyquery import PyQuery as pq
from pymongo import MongoClient

# url = https://m.weibo.cn/u/1259110474
# url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=1259110474&containerid=1076031259110474&page=2'
client = MongoClient()
db = client.weibo
collection = db.zly


def getJson(page):
    base_url = 'https://m.weibo.cn/api/container/getIndex?'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                     '(KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    data = {
        'type' : 'uid',
        'value' : 1259110474,
        'containerid' : 1076031259110474,
        'page':page
    }
    r = requests.get(base_url,params=data,headers = headers)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.json()

# nn = getJson(1)[0]
# print(nn)
# print(type(nn))
def parseJson(json):
    if json:
        items = json.get('data').get('cards')
        # print(items)
        for item in items:
            weibo = {}
            item = item.get('mblog', weibo)
            weibo['id'] = item.get('id')
            weibo['text'] = pq(item.get('text')).text()
            weibo['attitudes'] = item.get('attitudes_count')
            weibo['comments'] = item.get('comments_count')
            weibo['reposts'] = item.get('reposts_count')
            yield weibo
# nnn = parseJson(nn,1)
# for n in nnn:
#     print(n)

def save_page(result):
    if collection.insert(result):
        print('save success')

if __name__ == '__main__':
    for i in range(1,4):
        json = getJson(i)
        result = parseJson(json)
        for res in result:
            print(res)
            sleep(0.5)
            save_page(res)


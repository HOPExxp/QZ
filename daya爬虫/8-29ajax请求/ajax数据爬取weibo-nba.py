import requests
from fake_useragent import UserAgent
from pymongo import MongoClient
import time
from pyquery import PyQuery as pq

base_url = 'https://m.weibo.cn/api/container/getIndex?'
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
             '(KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
client = MongoClient()
db = client.weibo
collection = db.nba

def get_page(page):
    datas = {
        'type':'uid',
        'value':'1883881851',
        'containerid':'1076031883881851',
        'page':page
        }
    r = requests.get(base_url,params=datas,headers=headers)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.json(),page


def parse_page(json,page):
    if json:
        items = json.get('data').get('cards')
#enumerate函数将可遍历对象组成索引序列，枚举出数据和数据下标
        for index,item in enumerate(items):
            if page == 1 and index == 1:
                continue
            else:
                weibo = {}
                item = item.get('mblog',weibo)
                weibo['id'] = item.get('id')
                weibo['text'] = pq(item.get('text')).text()
                weibo['attitudes'] = item.get('attitudes_count')
                weibo['comments'] = item.get('comments_count')
                weibo['reposts'] = item.get('reposts_count')
                yield weibo

def save_page(result):
    if collection.insert(result):
        print('save success')

if __name__ == '__main__':
    for page in range(1,4):
        json = get_page(page)
        # print(type(json[0]))
        # print(type(json))
        results = parse_page(*json)#*json传值得一种方式，表示传可变参数
        for result in results:
            time.sleep(1)
            print(result)
            save_page(result)


# import requests
# from fake_useragent import UserAgent
# from pymongo import MongoClient
# import time
# from pyquery import PyQuery as pq
#
# base_url = 'https://m.weibo.cn/api/container/getIndex?'
# ua = UserAgent().chrome
# headers = {'User-Agent':ua}
# client = MongoClient()
# db = client.weibo
# collection = db.nba
#
# def get_page(page):
#     datas = {
#         'type':'uid',
#         'value':'1883881851',
#         'containerid':'1076031883881851',
#         'page':page
#         }
#     try:
#         response = requests.get(base_url,params=datas,headers=headers)
#         response.encoding = 'utf-8'
#         if response.status_code == 200:
#             return response.json(),page
#     except requests.ConnectionError as e:
#         print('Error',e.args)
#
# def parse_page(json,page):
#     if json:
#         items = json.get('data').get('cards')
# #enumerate函数将可遍历对象组成索引序列，枚举出数据和数据下标
#         for index,item in enumerate(items):
#             # if page == 1 and index == 1:
#             #     continue
#             # else:
#             weibo = {}
#             item = item.get('mblog',weibo)
#             weibo['id'] = item.get('id')
#             weibo['text'] = pq(item.get('text')).text()
#             weibo['attitudes'] = item.get('attitudes_count')
#             weibo['comments'] = item.get('comments_count')
#             weibo['reposts'] = item.get('reposts_count')
#             yield weibo
#
# def save_page(result):
#     if collection.insert(result):
#         print('save success')
#
# if __name__ == '__main__':
#     for page in range(1,4):
#         json = get_page(page)
# ##        print(type(json))
#         results = parse_page(*json)#*json传值得一种方式，表示传可变参数
#         for result in results:
#             # time.sleep(1)
#             print('1')
#             print(result)
#             # save_page(result)

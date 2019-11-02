# https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&
# offset=0&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&en_qc=1&
# cur_tab=1&from=search_tab&pd=synthesis&timestamp=1567179308522
# '''url = https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&
# offset=20&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&en_qc=1&
# cur_tab=1&from=search_tab&pd=synthesis&timestamp=1567179386771'''

# https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&
# offset=0&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&en_qc=1&
# cur_tab=1&from=search_tab&pd=synthesis&timestamp=1567342691351

import re
from time import sleep
import requests
from urllib.parse import urlencode

def getJson(offset):
    # url = '''https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&
    #     offset={}&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&en_qc=1&
    #     cur_tab=1&from=search_tab&pd=synthesis'''.format(str(offset))
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
    #                   '(KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    # }
    headers = {
        'cookie': 'tt_webid=6730888246245606919; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6730888246245606919; csrftoken=e2db0f1a785a00bb667d470f1c1330d5; s_v_web_id=1894bc528b463d558b2d9a3c9da2496a; __tasessionId=gj6tdd8jg1567171760330',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'referer': 'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D'
    }
    params = {
        'aid': '24',
        'app_name': 'web_search',
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'count': '20',
        'en_qc': '1',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis'
    }
    base_url = 'https://www.toutiao.com/api/search/content/?'
    url = base_url + urlencode(params)
    print(url)
    r = requests.get(url,headers = headers)
    r.raise_for_status()
    #为什么不能用这个？？？！！！
    # r.encoding = r.apparent_encoding
    return r.json()

# n = getJson(0)
# print(n)

def parseJson(json):
    if json.get('data'):
        items = json.get('data')
        # print(items)
        for item in items:
            #有image-list值的数据才有title，可以筛选出data中有image的内容
            if item.get('title') is None:
                continue
            title = item.get('title')
            # title = re.sub('[\t]', '', item.get('title'))
            # print(title)
            images = item.get('image_list')
            if images:
                # print(images)
                for image in images:
                    # url = image.get('url')
                    url = re.sub("list.*?pgc-image", "large/pgc-image", image.get('url'))
                    # print(url)
                    yield {
                        'title':title,
                        'image':url
                    }

# l = parseJson(n)
# print(l)
# print(l.__next__())


# def parseJson(json):
#     if json.get('data'):
#             items = json.get('data')
#             # print(items)
#             for item in items:
#                 title = item.get('title')
#                 images = item.get('image_list')
#                 print(images)
#                 for image in images:
#                     yield {
#                         'image':image.get('url'),
#                         'title':title
#                     }
#     else:
#         print('fail to get data')


# def saveImg(li):
#     for i in li:
#         r = requests.get(i)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         name = i.split('/')[-1] + '.jpg'
#         with open('./jiepai/%s'%name,'wb') as f:
#             f.write(r.content)
#             print('success')
# saveImg(l)

import os
from hashlib import md5
def saveImg(item):
    title = item.get('title').replace(':','：')
    title = title.replace('?','？')
    title = title.replace('|','-')
    title = title.replace('\\','-')
    title = title.replace('/','-')
    # os.path.sep  --  windows中的路径分隔符
    img_path = 'img' + os.path.sep + title
    # img_path = os.path.sep
    # print(img_path)
    if not os.path.exists(img_path):
        os.mkdir(img_path)
    #正式存储
    try:
        r = requests.get(item.get('image'))
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        # file_path = './jiepai/{}/{}.{}'.format(item.get('title'),md5(r.content).hexdigest(),'jpg')
        file_path = img_path + os.path.sep + '{file_name}.{file_suffix}'.format(
                file_name=md5(r.content).hexdigest(),
                file_suffix='jpg')
        if not os.path.exists(file_path):
            with open(file_path,'wb') as f:
                f.write(r.content)
            print('Downloaded image path is %s' % file_path)
        else:
            print('Already Downloaded', file_path)
    except Exception as e:
        print(e)

# for item in l:
#     saveImg(item)

def main(offset):
    json = getJson(offset)
    l = parseJson(json)
    for item in l:
        saveImg(item)

start = 1
end = 2

from multiprocessing.pool import Pool
if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(start,end)])
    pool.map(main, groups)
    pool.close()
    pool.join()
    # for i in range(4):
    #     json = getJson(i*20)
    #     # item = parseJson(json)
    #     # saveImg(item)
    #     for item in parseJson(json):
    #         print(item)
    #         print(1)
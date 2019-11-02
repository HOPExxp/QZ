import requests
from urllib.parse import urlencode
from requests import codes
import os
from hashlib import md5
from multiprocessing.pool import Pool
import re
import time


# 获取源码
def get_page(offset):
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
    try:
        resp = requests.get(url, headers=headers)
        if resp.status_code == 200:
            return resp.json()  # 格式根据response返回的类型来
    except requests.ConnectionError:  # 设置异常
        return None

n = get_page(0)
print(n)

# 获取图片名称及图片链接
def get_images(json):
    if json.get('data'):
        data = json.get('data')
        for item in data:
            if item.get('comments_count') is None:
                continue

            title = re.sub('[\W]', '', item.get('title'))  # 利用正则表达式来删除非字母、数字及下划线的字符
            images = item.get('image_list')
            for image in images:
                # 利用re.sub格式化image url
                origin_image = re.sub("list.*?pgc-image", "large/pgc-image", image.get('url'))
                yield {
                    'image': origin_image,
                    'title': title
                }


def save_image(item):
    # 定义存储图片的文件夹和路径,路径分隔符 C:\Users\Administrator\Desktop\img\'title'
    img_path = 'img' + os.path.sep + item.get('title')
    # 如果文件不存在则新建
    if not os.path.exists(img_path):
        os.makedirs(img_path)
        try:
            # 请求图片链接
            resp = requests.get(item.get('image'))
            if codes.ok == resp.status_code:
                # 定义文件路径，图片名称和后缀
                file_path = img_path + os.path.sep + '{file_name}.{file_suffix}'.format(
                    # 根据返回值得内容，利用md5来生成一个唯一的图片名称
                    filename=md5(resp.content).hexdigest(),
                    file_suffix='jpg')
                # 写入文件
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(resp.content)
            else:
                print('exists', file_path)
        except Exception as e:
            print(e)


def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        save_image(item)


# if __name__ == '__main__':
#     pool = Pool()
#     group = ([x * 20 for x in range(0, 3)])
#     pool.map(main, group)
#     pool.close()
#     pool.join()
#     time.sleep(3)
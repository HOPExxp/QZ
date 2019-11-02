
import re
import requests
import time
import json

# url_0 = 'https://maoyan.com/board/4?offset='
# headers = {
# 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36\
#              (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
# }
#
# for i in range(11):
#     url = url_0 + str(10*i)
#     html = requests.get(url ,headers = headers)
#
#     pattern = re.compile(
#         #排名
#         '<dd>.*?board-index.*?>(\d+)</i>'+
#         #图片地址
#         '.*?data-src="(.*?)"'+
#         #片名
#         '.*?class="name".*?title="(.*?)".*?'+
#         #主演
#         '.*?"star".*?\\n                (.*?)\n        </p>.*?'+
#         #上映时间
#         '.*?"releasetime">(.*?)</p>.*?'+
#         #豆瓣评分
#         '.*?"integer">(\d).*?"fraction">(\d)</i></p>',re.S
#     )
#
#     res = re.findall(pattern,html.text)
#     for i in res:
#         print(i)
#         with open('json.txt','a',encoding='utf-8') as f:
#             f.write(json.dumps(i,ensure_ascii=False)+'\n')
#     time.sleep(1)

def getHtmlText(url):
    try:
        headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36\
                     (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        }
        r = requests.get(url,headers = headers,timeout = 15)
        r.raise_for_status()#如果状态不是200,引发异常
        r.encoding = 'utf-8'
        return r.text
    except:
        return '1'

#一个生成器函数，包含解析出的结果，以字典形式保存
def praseHtml(html):
    pattern = re.compile(
            #排名
            '<dd>.*?board-index.*?>(\d+)</i>'+
            #图片地址
            '.*?data-src="(.*?)"'+
            #片名
            '.*?class="name".*?title="(.*?)".*?'+
            #主演
            '.*?"star".*?\\n                (.*?)\n        </p>.*?'+
            #上映时间
            '.*?"releasetime">(.*?)</p>.*?'+
            #豆瓣评分
            '.*?"integer">(\d).*?"fraction">(\d)</i></p>',re.S
        )
    res = re.findall(pattern , html)
    for item in res:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3],
            'time' : item[4],
            'score': item[5] + item[6]  # 将评分的2个数字合成一个
        }
def fill_file(content):
    with open('res.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')

def main(page):
    url =  'http://maoyan.com/board/4?offset=' + str(page)
    html = getHtmlText(url)
    #直接从解析过的生成器中取值，并保存到文件中
    for res in praseHtml(html):
        print(res)
        fill_file(res)

if __name__ == '__main__':
    for i in range(11):
        main(10 * i)
        time.sleep(1)
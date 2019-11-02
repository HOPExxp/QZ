# 需求：http://www.sodig.com/dir/人才招聘-公司企业/1/
# 用requests和正则表达式的方式获取该网站人才招聘页面下所有公司名称和网址，以json格式保存下来。
import re
import requests
import time
import json

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
        # 公司名称
        '.*?item-title">.*?>(.*?)</a>' +
        # 公司网址
        '.*?item-cat">\n                                                    \
(.*?)\n\n                                                </div>', re.S
        )
    res = re.findall(pattern , html)
    for item in res:
        yield {
            'company_name': item[0],
            'company_website': item[1],
        }
def fill_file(content):
    with open('8-15zy.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')

def main(page):
    url = 'http://www.sodig.com/dir/人才招聘-公司企业/{}/'.format(str(page))
    html = getHtmlText(url)
    #直接从解析过的生成器中取值，并保存到文件中
    for res in praseHtml(html):
        print(res)
        fill_file(res)

if __name__ == '__main__':
    for i in range(1,24):
        print(i)
        main(i)
        time.sleep(1)
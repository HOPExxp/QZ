#返回网页的标题
import requests
from bs4 import BeautifulSoup
import re
import json
def getHtmlText_Key(key):
    url = 'http://www.baidu.com/s?wd=' + key
    try:
        f = requests.get(url,timeout = 15)
        f.raise_for_status()
        f.encoding = 'utf-8'
        return f.text
    except:
        return 'F'
def parserHtml(html):
    soup = BeautifulSoup(html,'html.parser')
    links = []
    for i in soup.find_all('em'):
        links.append(i.string)
    return links
def main():
    html = getHtmlText_Key('python语言程序基础设计基础(第二版)')
    ls = parserHtml(html)
    count = 1
    for j in ls[:5]:
        print('[{:^3}]{}'.format(count,j))
        count += 1
main()
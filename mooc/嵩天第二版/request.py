import requests
from bs4_test import BeautifulSoup
def getHtmlText(url):
    try:
        r = requests.get(url,timeout = 15)
        r.raise_for_status()#如果状态不是200,引发异常
        r.encoding = 'utf-8'
        return r.text
    except:
        return '1'

url = 'http://www.baidu.com'
text = getHtmlText(url)
soup = BeautifulSoup(text)
print(soup)
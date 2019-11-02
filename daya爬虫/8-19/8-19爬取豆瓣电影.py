from bs4 import BeautifulSoup
import requests


def getHtml(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36\
                             (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        }
        r = requests.get(url,headers = headers)
        r.raise_for_status()
        r.encoding('utf-8')
        return r.text
    except:
        print('1')
def parseHtml(html):
    pass


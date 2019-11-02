import requests
from lxml import etree

def handle_douyin_web_share():
    share_web_url = 'https://www.douyin.com/share/user/88445518961'
    share_web_header = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    share_web_response = requests.get(url = share_web_url,headers = share_web_header)
    share_web_html = etree.HTML(share_web_response.text)
    nickname = share_web_html.xpath('//p[@class="nickname"]/text()')
    print(nickname)
handle_douyin_web_share()
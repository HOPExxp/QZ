import requests
from lxml import etree

# url = 'https://s.taobao.com/search?initiative_id=tbindexz_20170306&ie=utf8&spm=a21bo.2017.201856-taobao-item.2&sourceId=tb.index&search_type=item&ssid=s5-e&commend=all&imgfile=&q=ipad&suggest=history_1&_input_charset=utf-8&wq=&suggest_query=&source=suggest'
# url = 'https://s.taobao.com/search?q=ipad&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306'
# url = 'https://s.taobao.com/search?q=ipad&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306'
url = 'https://movie.douban.com/top250'
# headers = {
# 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36\
#              (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
# }
headers = {
'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) \
Chrome/63.0.3239.132 Safari/537.36'
}
try:
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    txt = r.text
    # print(txt)
except:
    print("false")

html = etree.HTML(txt)
# print(html)
items = html.xpath('//div[@class="item"]')
# print(items)
print(len(items))
# for item in items:
paiming = html.xpath('//em/text()')
print(paiming)
print(len(paiming))
links = html.xpath('//div[@class="pic"]/a/img/@src')
print(links)
print(len(links))
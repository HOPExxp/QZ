import requests
from lxml import etree
import json
#1.获取请求
url = 'http://music.taihe.com/top/dayhot'
base_url = 'http://musicapi.taihe.com/v1/restserver/ting?method=baidu.ting.song.playAAC&songid='
html = requests.get(url).content.decode('utf-8')
print(html)
#解析html
dom = etree.HTML(html)
ids = dom.xpath('//a[contains(@href,"/song/")]/@href')[4:]
# print(len(ids))
for id in ids:
    music_id = id.split('/')[-1]
    # print(music_id)
    finall_url = base_url + '%s'%music_id
    # print(finall_url)
    html1 = requests.get(finall_url).text
    #此html包含json格式，需解析
    # print(html1)
    dict_url = json.loads(html1)
    # print(dict_url)
    result_song_url = dict_url['bitrate']['file_link']
    # print(result_song_url)

    song = requests.get(result_song_url).content
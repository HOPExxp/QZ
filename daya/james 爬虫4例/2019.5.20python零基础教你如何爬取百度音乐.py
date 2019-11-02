
# # 0.导入框架(库,模块)  pip install requests
# import requests
#
# # 1.确定url
# url = 'http://zhangmenshiting.qianqian.com/data2/music/0027f238900cf186f6d5c909513c2b4d/612356196/612356196.mp3?xcode=562fceebb1119c89e4d6351b3c1b445d'
# url1 = 'http://audio01.dmhmusic.com/71_53_T10046455719_128_4_1_0_sdk-cpm/0210/M00/6B/57/ChR461tYzIWAI7uRADirJWcZUEM718.mp3?xcode=aaaca28d0fd551df4c84daebf65ee2e234a81de'
# # 2.发起请求下载
# music = requests.get(url1).content
#
# with open('./001.mp3', 'wb') as f:
#     f.write(music)


# # http://music.taihe.com/top/dayhot
# # 0.导入框架(库,模块)
# import requests
# from lxml import etree
# import json
#
# # 1.确定url
# url = 'http://music.taihe.com/top/dayhot'
# base_url = 'http://musicapi.taihe.com/v1/restserver/ting?method=baidu.ting.song.playAAC&songid='
#
#
# # 2.请求数据   xml   json
# text = requests.get(url).content.decode('utf-8')
# # print(text)
#
# # 3.调整方法,删选数据
# dom = etree.HTML(text)
# ids = dom.xpath('//a[contains(@href,"/song/")]/@href')[3:]
# # print(ids)
# # # 4.下载保存
# for index, id in enumerate(ids):
#     print(index,id)
#     resust_id = id.split('/')[-1]
#     # print(index, resust_id)
#
#     song_url = base_url + '%s' % resust_id
#     # print(song_url)
#     song_url_string = requests.get(song_url).text
#
#     dict_url = json.loads(song_url_string)
#     result_song_url = dict_url['bitrate']['file_link']
#     #print(result_song_url)
#
#     song = requests.get(result_song_url).content
#
#     # 语法    w表示写入   b表示二进制的方式
#     with open('./movie.mp3','wb') as file:
#         file.write(song)



#
# #*******************千千音乐
# import requests
# from lxml import etree
# import json
#
# # 1.确定url
# url = 'http://music.taihe.com/top/dayhot'
# base_url = 'http://musicapi.taihe.com/v1/restserver/ting?method=baidu.ting.song.playAAC&songid='
#
#
# # 2.请求数据   xml   json
# text = requests.get(url).content.decode('utf-8')
# # print(text)
#
# # 3.调整方法,删选数据
# dom = etree.HTML(text)
# ids = dom.xpath('//a[contains(@href,"/song/")]/@href')[3:]
#
# # 4.下载保存
# for index, id in enumerate(ids):
#
#     resust_id = id.split('/')[-1]
#     # print(index, resust_id)
#
#     song_url = base_url + '%s' % resust_id
#     # print(song_url)
#     song_url_string = requests.get(song_url).text
#
#     dict_url = json.loads(song_url_string)
#     # print(dict_url)
#     result_song_url = dict_url['bitrate']['file_link']
#     print(result_song_url)
#
#     song = requests.get(result_song_url).content

#     # 语法    w表示写入   b表示二进制的方式
#     with open('./movie.mp3','wb') as file:
#         file.write(song)
#





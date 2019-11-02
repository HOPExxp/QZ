# import requests
#
# url = 'https://m701.music.126.net/20190718091213/793b85761c676733425b41a42f35bbbf/jdyyaac/560c/0358/0608/af80b353a142fa9fe3c61ba8953ab433.m4a'
# url1 ='https://m701.music.126.net/20190718102943/c678a5c0736c1ff93c736d3c15010002/jdyyaac/560c/0358/0608/af80b353a142fa9fe3c61ba8953ab433.m4a'
# html = requests.get(url1).content
#
# with open('./wangyiyun.m4a','wb') as f:
#     f.write(html)

#1.导入库
import requests
from lxml import etree
import re
from bs4_test import  BeautifulSoup
#2.发起请求
url = 'https://music.163.com/playlist?id=2873390435'
# base_url1 = 'https://link.hhtjim.com/163/'
base_url ='https://link.hhtjim.com/163/'
html = requests.get(url).text
# print(html)

#3.解析html,筛选数据  dom格式：文档对象模型
dom  = etree.HTML(html)
#用xpath解析这种树形结构
ids = dom.xpath('//a[contains(@href,"/song?")]/@href')
print(ids)

#用BeautifulSoup解析html
# soup = BeautifulSoup(html,'html.parser')
# ids1 = soup.find_all('a',{'href':re.compile('song')})
# for id in ids1:
#     try:
#         if '$' not in id.string and id.string != '':
#             name = id.string
#     except:
#         pass

for id in ids:
    id_single = id.strip('/song?id=')
    if '$' not in id_single:
        # print(id_single)
#外链地址  https://link.hhtjim.com/163/1377450530.mp3
        finall_url = base_url + '%s'%id_single + '.mp3'
        # print(finall_url)
        song_name = finall_url.split('/')[-1]
        content = requests.get(finall_url).content

        with open('./WyyMusic/wyy%s' % song_name, 'wb') as f:
            f.write(content)




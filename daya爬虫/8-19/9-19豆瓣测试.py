from bs4 import BeautifulSoup
import requests
import time
import json

url = 'https://movie.douban.com/top250'
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36\
             (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
html = requests.get(url ,headers = headers).text

soup = BeautifulSoup(html,'html.parser')

# data = soup.find_all('div',attrs={'class','item'})
#
# paiming = data.find_all('em',class_='')
#
# print(paiming)

for data in soup.find_all('div',class_='item')[:5]:
    #排名信息
    # for item0 in data.find_all('em',class_=''):
    #     pass
    #     # print(item0.string)
    # #电影名
    # for item1 in data.find_all('span',class_='title')[::2]:
    #     pass
    #     # print(item1.string)
    # #描述信息
    # for item2 in data.find_all('p',class_=''):
    #     pass
    #     # print(item2.get_text().strip())
    # #评分
    # for item3 in data.find_all('span',class_='rating_num'):
    #     pass
    #     # print(item3.string)
    item0 = data.find_all('em',class_='')
    # print(i.string for i in item0)
    # for i in item0:
    #     print(i.string)
    item1 = data.find_all('span',class_='title')[::2]
    item2 = data.find_all('p',class_='')
    item3 = data.find_all('span',class_='rating_num')

    with open('douban.txt','a',encoding='utf-8') as f:
        for a,b,c,d in zip(item0,item1,item2,item3):
            # print(a.string,b.string,c.get_text().strip(),d.string)
            rank = str('>' * 20 + 'Top：' + a.get_text() + '<' * 20)
            name = str('电影名：' + b.get_text())
            msg = str('电影信息：' + c.get_text().strip())
            score = str('评分：' + d.get_text())
            f.write('\n'.join([rank, name, msg, score]))
            f.write('\n' * 2)
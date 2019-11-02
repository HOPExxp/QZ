import requests
from lxml import etree
import re
from bs4_test import BeautifulSoup
url = 'https://music.163.com/playlist?id=2869035742'
html = requests.get(url).text
# print(html)
#################
# dom = etree.HTML(html)
# ids = dom.xpath('//a[@href]/@href')
# print(ids)
##################
soup = BeautifulSoup(html,'html.parser')
ids = soup.find_all('a',{'href':re.compile('song')})
for id in ids:
    try:
        if '$' not in id.string and id.string != '':
            print(id.string)
    except:
        pass
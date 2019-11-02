import requests
from bs4_test import BeautifulSoup
list = []
#获取网页文本
def getHtmlText(url):
    try:
        r = requests.get(url,timeout = 15)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return 'F'
#将所得文本存入列表中
def fill_list(soup):
    data = soup.find_all('tr')
    for l in data:
        lie = l.find_all('td')
        if len(lie) == 0:
            continue
        s_list = []
        for i in lie:
            s_list.append(i.string)
        list.append(s_list)
def printList(num):
    # print('{:^4}{:^10}{:^5}{:^8}{:^10}'.format('排名','学校名称','省份','总分','科研规模'))
    print('{1:^4}{2:{0}^10}{3:{0}^5}{4:{0}^8}{5:{0}^10}'.format(chr(12288),'排名','学校名称','省份','总分','科研规模'))
    for k in range(num):
        u = list[k]
        # print('{:^4}{:^10}{:^5}{:^8}{:^10}'.format(u[0],u[1],u[2],u[3],u[6]))
        print('{1:^4}{2:{0}^10}{3:{0}^5}{4:{0}^8.1f}{5:{0}^10}'.format(chr(12288),u[0],u[1],u[2],eval(u[3]),u[6]))
def main(num):
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    html = getHtmlText(url)
    soup = BeautifulSoup(html,'html.parser')
    fill_list(soup)
    printList(num)
main(10)

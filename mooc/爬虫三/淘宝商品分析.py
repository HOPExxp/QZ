import requests
import re

def gethtmltext(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        # print(r.status_code)
        r.encoding =r.apparent_encoding
        return r.text
    except:
        print("1")

def parsepage(ili,html):
    try:
        #json方法?
        #beautifulsoup方法?
        pli = re.findall(r'\"view_price\"',html)     #未解析到数据！！
        tli = re.findall(r'"raw_title":".*?"',html)           #html中没有相应内容，
        print(pli)                                                      #另写程序单独输出html的内容
        # print(tli)
        for i in range(len(pli)):
            price = eval(pli[i].split(':')[1])
            title = eval(tli[i].split(':')[1])
            ili.append([price,title])
    except:
        print("2")

def printgoodslist(ili):
    try:
        tpli="{:4}\t{:8}\t{:16}"
        print(tpli.format("序号","价格","商品名称"))
        count=0
        for g in ili:
            count+=1
            print(tpli.format(count,g[0],g[1]))
    except:
        print("3")

def main():
    goods='背包'
    depth=2
    start_url='http://s.taobao.com/search?q=%E8%83%8C%E5%8C%85'
    goodslist=[]
    for i in range (depth):
        try:
            url=start_url+'&s='+str(44*i)
            html=gethtmltext(url)
            # print(url)
            parsepage(goodslist ,html)
        except:
            print("4")
    printgoodslist(goodslist)

main()



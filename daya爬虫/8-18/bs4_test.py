html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
and they lived at the bottom of a well.</p>
<p class="story">...</p>
<html>
"""
from bs4 import BeautifulSoup

# soup=BeautifulSoup(html,'lxml')
#
# #基本用法
# print(soup.prettify())#把解析的字符串以标准的缩进格式输出
# print(soup.title.string)#调用string获取title文本内容
#
# #1.选择元素
# print(soup.head)#全部内容
# print(soup.p)#当有多个节点的时候，只会返回第一个节点
#
# #2.提取信息
# #-1节点名称name
# print(soup.head.name)
# #-2节点属性和值
# print(soup.p.attrs)
# print(soup.p.attrs['name'])
# #-3获取节点内容
# print(soup.p.string)

#3.嵌套选择  sb

#4.关联选择
#选取某个节点为基准再选择它的子节点、父节点、兄弟节点，这种叫做关联选择
html1 = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
"""
from bs4 import BeautifulSoup

soup=BeautifulSoup(html1,'lxml')
#print(soup.prettify())
print(soup.p.contents)
print('-------------------')
print(soup.p.children)
#enumerate()函数可以将一个可遍历的数据对象（list 元组，字符串等）组合成一个 索引序列，同时列出数据和数据下标
for a,child in enumerate(soup.p.children):
    print(a,child)
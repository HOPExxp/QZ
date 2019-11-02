text = '''
<?xml version="1.0" encoding="utf-8"?>

<bookstore>

<book>
  <title lang="eng">Harry Potter</title>
  <price>29.99</price>
</book>

<book>
  <title lang="eng">Learning XML</title>
  <price>39.95</price>
</book>

</bookstore>
'''

from lxml import etree
html = etree.HTML(text)     #html对象
print(etree.tostring(html).decode('utf-8'))

#基本语法
# res = html.xpath('/html')
# res1 = html.xpath('//bookstore/book')
# res2 = html.xpath('//bookstore//book')
# res3 = html.xpath('/html//title/@lang')
# print(res)
# print(res1)
# print(res2)
# print(res3)

#谓语
# res = html.xpath('/html//book[1]')
# res1 = html.xpath('/html//book[last()]')
# res2 = html.xpath('/html//book[position()=1]')
# res3 = html.xpath('//title[@lang]/@lang')
# res4 = html.xpath('/html//book[price>35.00]')
# print(res)
# print(res1)
# print(res2)
# print(res3)
# print(res4)

#选取若干路径
res = html.xpath('/html//book/title | //price')
print(res)
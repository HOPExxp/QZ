# text = '''
# <div>
#     <ul>
#          <li class="item-0"><a href="link1.html">first item</a><>
#          <li class="item-1"><a href="link2.html">second item</a><>
#          <li class="item-inactive"><a href="link3.html">third item</a><>
#          <li class="item-1"><a href="link4.html">fourth item</a><>
#          <li class="item-0"><a href="link5.html">fifth item</a>
#      </ul>
#  </div>
# '''

#处理html类型的字符串
# from lxml import etree
# html = etree.HTML(text)     #html对象
# print(type(html))
# byte_html = etree.tostring(html)  #字节形式html
# print(type(byte_html))
# # print(byte_html.decode('utf-8')) #文档对象类型 -- DOM树
# res = byte_html.decode('utf-8')
# print(res)

#_-------------------------
# #也可以直接处理保存在文件中的html
# html = etree.parse('html_txt.txt',etree.HTMLParser(),)
# res1 = etree.tostring(html).decode('utf-8')
#
# #检查结果
# print(res)
# print()
# print(res1)
#_--------------------------

#查找元素节点时直接使用html对象即可

# # //
# result = html.xpath('//li[@class="item-0"]//text()')
# print(result)

text = '''
<li class="li li-first" name="item"><a href="link.html">first item</a></li>
<li class="li li-first"><a href="link.html">second item</a></li>
'''

from lxml import etree
html = etree.HTML(text)
result = html.xpath('//li[@class="li li-first" and @name="item"]/a/text()')
print(result)

html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''

from pyquery import PyQuery  as  py

# doc = py(html)
# print(doc)
# print('-------------')
# items = doc('.list')
# print(type(items))
# items1 = doc.find('.list')
# print(items1)
# print(type(items1))

# 子节点
# print(doc.children().children('.item-0'))
# 父节点
# print(items.parent())
# print('--------')
# parents = items.parents()
# print(parents)

# 获取属性值
# doc = py(html)
# a = doc('.item-0.active a')
# print(a.text())#获取文本值
# print(a.html())#获取html文本
#
# print('----------------------')
# a = doc('a')
# for item in a.items():
#     print(item.attr('href'))

# addClass和removeClass（增加和删除class）
# doc = py(html)
# li = doc('.item-0.active')
# print(li)
# li.removeClass('active')
# print(li)
# li.addClass('active')
# print(li)

# attr()方法修改属性值
# text()和html()方法来改变节点内部的内容
# 示例：
html = '''
<ul class="list">
     <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
</ul>
'''

from pyquery import PyQuery as pq

doc = pq(html)
li = doc('.item-0.active')
print(li)
li.attr('name','wang')
print(li)
li.text('chang 1 2 3 5')
print(li)
li.html('<a href="link3.html"><span class="bold">third item</span></a>')
print(li)
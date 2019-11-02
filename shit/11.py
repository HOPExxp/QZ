html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''

from pyquery import PyQuery as pq
doc = pq(html)

li1 = doc('li:first-child')          #第一个li节点
li2 = doc('li:last-child')           #最后一个li节点
li3 = doc('li:nth-child(2n)')       #偶数位置的li节点
li4 = doc('li:contains(second)')    #包含second文本的li节点
print(li1)
print(li2)
print(li3)
print(li4)
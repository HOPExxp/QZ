text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html"><span>first item</span></a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''

from lxml import etree
html = etree.HTML(text)
# result = etree.tostring(html)
# print(result.decode())
result1 = html.xpath('//li[1]/ancestor::*')
print(result1)
result2 = html.xpath('//li[1]/ancestor::html')
print(result2)
result3 = html.xpath('//li[1]/attribute::*')
print(result3)
result4 = html.xpath('//li[1]/a/attribute::*')
print(result4)
result5 = html.xpath('//li[1]/following-sibling::*')
print(result5)
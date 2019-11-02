import jieba
res = jieba.cut('中华人民共和国是一个伟大的国家')
print(type(res),res)
li = list(res)
print(li)
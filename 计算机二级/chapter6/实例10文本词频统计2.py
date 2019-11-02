import jieba

#基本值
txt = open('threekingdoms.txt','r',encoding='utf-8').read()
words = jieba.lcut(txt)
counts  = {}

#处理
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word,0) + 1

#去掉不是人名的分词
for w in ['将军','却说','二人','不可','荆州','不能','如此','商议','如何']:
    del counts[w]


#将字典count转为列表，方便排序
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse = True)
for i in range(10):
    word , count = items[i]
    print('{:<10}{:<5}'.format(word,count))

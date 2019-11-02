def getText():
    txt = open('hamlet.txt','r').read()
    txt = txt.lower()
    for ch in '!@#$%^&*()_+:;"\',<.>/?[]{}\|':
        txt = txt.replace(ch,' ')
    return txt
hamlettxt = getText()
# print(hamlettxt)

#基本值
words = hamlettxt.split()
count = {}
except_words = ['the','and','to','of','a','in','it','i','my','you','is','not','that',\
                'his','this','for','your','s','me','but','with','he','be','as','him','so']

#将每个词统计好
for word in words:
    count[word] = count.get(word,0) + 1

#去掉一些无实意的词
for w in except_words:
    del count[w]

#将字典count转为列表，方便排序
items = list(count.items())
items.sort(key=lambda x:x[1],reverse = True)
for i in range(10):
    word , count = items[i]
    print('{:<10}{:<5}'.format(word,count))
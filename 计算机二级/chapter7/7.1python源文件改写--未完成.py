
import keyword
# tf = keyword.iskeyword('fwweaf')
words = keyword.kwlist
# print(tf)
print(words)


fr = open('7.1yuanma.py','r',encoding='utf-8')
for i in fr:
    i = i.replace('\n','')
    # print(type(i))
    # print(i)
    print(i.upper())

    # words = i.split()
    # # print(words)
    # # w = ' '.join(words)
    # # print(w)
    #
    # for word in words:
    #     s = i
    #     if keyword.iskeyword(word):
    #         continue
    #     else:
    #         # print('1')
    #         s.replace(word,word.upper())
    #         print(s)
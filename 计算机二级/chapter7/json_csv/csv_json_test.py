#将csv格式数据转换成  [  { , }  , { , }  ,  ] 格式的二维数据
#先逐行加入一个列表中(逐行append),每一行也是一个列表(split)
#csv数据的第一行是标题，将此行的信息与其他行组成一个关系对，进而形成一个键值对的形式（字典）
#保存为json格式数据在文件中

import json
fr = open('price2016.csv','r',encoding='utf-8')
ls = []
for l in fr:
    l = l.replace('\n','')
    ls.append(l.split(','))
fr.close()
# fw = open('price2016_2.json','w',encoding='utf-8')
for i in range(1,len(ls)):
    ls[i] = list(zip(ls[0],ls[i]))
print(ls)

#不要sort_keys即可，sort后反而会改变顺序影响数据观看

# json.dump(ls[1:],fw,sort_keys=True,indent=4,ensure_ascii=False,)
# fw.close()
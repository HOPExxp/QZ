#从文件中加载数据，json格式转为了原来的数据类型
import json
fr = open('price2016_2.json','r',encoding='utf-8')

ls = json.load(fr)

#将字典转成原来的列表形式

#  ls[0]  --  列表的第一个值-字典，每个字典的key值都相同
#只包含标题信息
data = [list(ls[0].keys())]
#加入数据信息
for item in ls:
    data.append(list(item.values()))
fr.close()

#再次用csv格式保存   --  列表到用逗号分隔即可保存为csv格式
fw = open('price2016_from_json2.csv','w',encoding='utf-8')
for i in data:
    fw.write(','.join(i)+'\n')
fw.close()
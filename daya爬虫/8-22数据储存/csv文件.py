import csv
# 单行输入
with open('data.csv','w',encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['id','name','age'])
    writer.writerow(['1','feiyu','18'])
    writer.writerow(['2','079','18'])
    writer.writerow(['3','123','18'])

# 多行输入
with open('data1.csv','w',encoding='utf-8') as g:
    writer = csv.writer(g)
    writer.writerow(['id','name','age'])
    li = [['1','feiyu','18'],['2','079','18'],['3','123','18']]
    writer.writerows(li)

#字典方式写入
with open('data2.csv','w',encoding='utf-8') as h:
    title = ['id','name','age']
    # 初始化写入对象
    writer = csv.DictWriter(h,fieldnames=title)
    writer.writeheader()
    writer.writerow({'id': '35', 'name': 'james', 'age': '35'})
    writer.writerow({'id': '1', 'name': 'harden', 'age': '32'})
    writer.writerow({'id': '32', 'name': 'jordon', 'age': '60'})

# 读取文件内容
import csv

with open('data.csv','r',encoding='utf-8') as f:
    reader = csv.reader(f)#调用CSV库的reader方法，传入别名
    for row in reader:
        print(row)
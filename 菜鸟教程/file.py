file = open(r'C:\Users\xxp\PycharmProjects\cxdm\python全栈 书籍\chap1词频统计\xyj.txt','r',encoding='utf-8')
r = file.read(2)
while r != '':
    r = file.read(2)
    print(r)
#指针在文件开始
# print(file.tell())

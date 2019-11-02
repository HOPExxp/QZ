#手动输入五个数
#是奇数，乘20；是偶数，除20。
#判断输入的数是否相等
# numbers=[]
# while True :
#     l=input('请输入一个数：')
#     numbers.append(l)
#     if l=='':
#         break
# print(numbers[0:len(numbers)-1])
numbers=[]
while True :
    l=input('请输入一个数：')
    if l in numbers:
        print('你输入的数已经存在')
        continue
    numbers.append(l)
    if len(numbers)==5:
        break
for i in  numbers:
    try:
        if eval(i)%2!=0:
            print(eval(i),'是一个奇数，和20相乘:',eval(i)*20)
        elif eval(i)%2==0:
            print(eval(i),'是一个偶数，和20相除:',eval(i)/20)
        else:
            pass
    except:
        print('没有数据，程序结束')
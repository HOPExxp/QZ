li=[]
while True :
    l=input('请输入一个字符串')
    li.append(l)
    if len(li)==10 :
        break
#print(li)
for i in li :
    for j in i :
        if j.islower() :
            print(j.upper(),end='')
        elif j.isupper() :
            print(j.lower(),end='')
    print()


#统计不同字符个数
#字典 或  直接

#直接
english = 0
num = 0
space = 0

content = input('>>')

other = len(content)
for i in content:
    if i.isspace():
        space += 1
        other -= 1
    if i.isalpha():
        english += 1
        other -= 1
    if i.isdecimal():
        num += 1
        other -= 1
    # #判断是否符合标识符规则，这个要求中不满足（下划线）
    # if i.isidentifier():
    #     other += 1
print('总字符数{} 英文字符数{} 数字字符数{} 空格字符数{} 其他字符数{}'.format(len(content),english,num,space,other))
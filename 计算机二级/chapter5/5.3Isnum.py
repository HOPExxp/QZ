def isNum(str):
    print(str.isdecimal)
    #加括号
    if str.isdecimal():
        return True
    else:
        return False
str = input('>>')
res = isNum(str)
print(res)
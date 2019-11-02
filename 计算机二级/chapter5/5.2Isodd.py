def isOdd(num):
    if num % 2 == 1:
        return True
    else:
        return False
n = int(input('>>'))
res = isOdd(n)
print(res)
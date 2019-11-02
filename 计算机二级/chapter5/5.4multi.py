#返回所有参数的乘积
def multi(*args):
    res = 1
    for i in args:
        res *= i
    return res
res = multi(1,2,3,4,5)
print(res)
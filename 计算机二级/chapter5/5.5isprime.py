def isPrime(num):
    if num.isdecimal():
        if isinstance(eval(num),int):
            if eval(num) % 2 == 1:
                print('奇数')
            else:
                print('偶数')
        else:
            print('是数字类型，但不是整数')
    else:
        print('非数字类型')
while True:
    str = input('>>')
    isPrime(str)
#猜数游戏

from random import randint
#答案
a = randint(1,9)
nums = 1
while True:
    # b = int(input('>>'))
    # if not isinstance(b,int):
    #     print('输入内容必须为整数！请重新输入')
    #     continue
    b = input('>>')
    if b.isdecimal():
        if isinstance(int(b),int):
            b = int(b)
    else:
        print('输入内容必须为整数！请重新输入')
        continue
    if b > a:
        print('遗憾，太大了')
        nums += 1
    elif b < a:
        print('遗憾，太小了')
        nums += 1
    else:
        print('预测了{}次，你猜中了！'.format(nums))
        break
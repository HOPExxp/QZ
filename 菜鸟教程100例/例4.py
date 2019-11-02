# 题目：输入某年某月某日，判断这一天是这一年的第几天？
#
# 程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：
import math
def getYearNum():
    n = int(input('请输入年份:'))
    i = int(input('请输入月份:'))
    r = int(input('请输入日期:'))
    t= 0
    # for i in range(1,y +1):
    if i <= 2:
        t = 31 +  r
    elif i>2 and i % 2 == 0:
        if (n % 400 == 0) or ((n % 4 == 0) and (n % 100 != 0)):
        # if n % 4 == 0:
            t= 31 * ((i / 2)-1) + 28 + 30 * ((i / 2)-1) + r
        else:
            t = 31 * ((i / 2) - 1) + 29 + 30 * ((i / 2) - 1) + r
    elif i>2 and i % 2 == 1:
        if (n % 400 == 0) or ((n % 4 == 0) and (n % 100 != 0)):
        # if n % 4 == 0:
            t = 31 * int(i / 2) + 28 + 30 * ((int(i / 2)-1)) + r
        else:
            t = 31 * int(i / 2) + 29 + 30 * ((int(i / 2) - 1)) + r
    return t
print(getYearNum())

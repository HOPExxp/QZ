#最大公约数  最小公倍数计算

# #最大公约数
# a = int(input('>>'))
# b = int(input('>>'))
# for i in range(-min(a,b),-1):
#
#     #  1
#     # if str(a/(-i)).isdecimal and str(b/(-i)).isdecimal:
#     #     print(i)
#
#     #  2
#     # print(isinstance(a/(-i),int),isinstance(b/(-i),int))
#     # print(a/(-i),b/(-i))   -->>为浮点数 4.0 2.0
#     # if isinstance(a/(-i),int) and isinstance(b/(-i),int):
#     #     print(i)
#
#     #  3
#     if a/(-i)%1 == 0 and b/(-i)%1 == 0:
#         print(i)
#         break

#最小公倍数
from math import inf
a = int(input('>>'))
b = int(input('>>'))
for i in range(max(a,b),a*b+1):
    if i/a%1 == 0 and i/b%1 == 0:
        print(i)
        break



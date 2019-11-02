# 生日悖论，指如果一个房间里有23个或23个以上的人，那么至少有两个人的生日相同的概率要大于50%。
# 这就意味着在一个典型的标准小学班级(30人)中，存在两人生日相同的可能性更高。
# 对于60或者更多的人，这种概率要大于99%。从引起逻辑矛盾的角度来说生日悖论并不是一种悖论，
# 从这个数学事实与一般直觉相抵触的意义上，它才称得上是一个悖论。
# 大多数人会认为，23人中有2人生日相同的概率应该远远小于50%。
# 计算与此相关的概率被称为生日问题，在这个问题之后的数学理论已被用于设计著名的密码攻击方法:生日攻击。


from random import *


def sam():
    brithday = []
    res = []
    for i in range(1000):
        n = randint(1, 365)
        brithday.append(n)

    for j in range(23):
        k = brithday[randint(0, 999)]
        res.append(k)

    for i in range(1, 23):
        for j in range(i):
            if res[i] == res[j]:
                return True
    return False


counts = 0
for i in range(100):
    if sam():
        counts += 1
    else:
        continue
print("至少两人相同的概率是{}%".format(counts))



#     -----2---------
# import random
#
# def bdp(n,k):
#
#     cv = []
#
#     for i in range(k):
#
#         m = []
#
#         for j in range(n):
#
#             m.append(random.randint(1,365))
#
#         counter = 0
#
#         for k1 in m:
#
#             for k2 in m:
#
#                if k1 == k2:
#
#                     counter += 1
#
#         cv.append(float(counter/2)/float(n))
#
#         ss = 0
#
#         for i in cv:
#
#             ss += i
#
#         return ss/float(len(cv))
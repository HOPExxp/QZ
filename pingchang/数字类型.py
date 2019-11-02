import math
import random
# # print(math.modf(1.3))
# a,b = math.modf(2.3)
# print(a)
# print(b)
# print(math.sqrt(4))
#从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
c = random.choice(range(9))
#随机生成下一个实数，它在[0,1)范围内
c = random.random()
#	随机生成下一个实数，它在[x,y]范围内
c = round(random.uniform(2,3),2)
#	将序列的所有元素随机排序
#   errors:  for i in reversed(range(1, len(x))):
# TypeError: object of type 'int' has no len()
list = [1,2,3,4,5,6,7,8]
random.shuffle(list)
print(list)
#从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1
c = random.randrange(2,10,2)
print(c)

print(math.pi)
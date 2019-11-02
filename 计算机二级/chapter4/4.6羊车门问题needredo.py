# #羊车门问题
# import random
# # qiche_num = random.randint(1,3)
#
# dic = {
#     1:'汽车',
#     2:'羊',
#     3:'羊'
# }
#
# print(random.choice(dic))
# # chioce = int(input('输入1/2/3>>'))
# #
# # if dic[chioce] != '羊':
# #     zcr_chioce = random.choice(dic)


#**********标准答案

import random
#试验次数 ？？
x=random.randint(5000,10000)
#
change=0
nochange=0
for i in range(1,x+1):
    #原来的选择和更改后的选择，
  a=random.randrange(1,4)
  b=random.randrange(1,4)
    #相等即为不改变选择
  if a==b:
    nochange=nochange+1
    #不相等即为改变选择
  else:
    change=change+1
print("不更改选择得到汽车的概率为{}".format(nochange/x))
print("更改选择得到汽车的概率为{}".format(change/x))


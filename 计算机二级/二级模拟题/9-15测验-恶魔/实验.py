#9
# ds = {'eng':2,'math':6,'comp':9,'PE':4}
# print(ds.pop(max(ds.keys())),0)

#10
# with open('a.txt','r') as f:
#     print(f.read().split(','))

#操作1
# studs= [{'sid':'103','Chinese': 90},{'sid':'101','Chinese': 80},{'sid':'102','Chinese': 70}]
# scores = {}
# for stud in studs:
#     #字典items列表
#     sv = stud.items()
#     for it in sv:
#         #it--字典的每一个键值对元组
#         if it[0] =='sid':
#             #学号值
#             k = it[1]
#         else:
#             scores[k] = it[1]
# # print(scores)
# so = list(scores.items())
# # print(so)
# so.sort(key = lambda x:x[0],reverse = False)
# for l in so:
#     print('{}:{}'.format(l[0],l[1]))

#操作4
# flag = 1
# while flag:
#     try:
#         n = eval(input())
#         xin = input().split(',')
#         yin = input().split(',')
#         if n == len(xin) and n == len(yin):
#             sum = 0
#             for i in range(n):
#                 sum += int(xin[i]) * int(yin[i])
#             print("x和y的内积是:", sum)
#             break
#     except:
#        print("请输入整数！")
#        continue


#操作5
fi = open("xueyajilu.txt", 'r',encoding="utf-8")
jl = [[], [], [], [], [], []]  # 1:zb_h, zb_l,yb_h,yb_l
#左压差
zyc = []
#右压差
yyc = []
#心率
xl = []
for l in fi:
    lls = l.split(",")

    for i in range(6):
        jl[i].append(lls[i])

    zyc.append(eval(lls[1]) - eval(lls[2]))
    yyc.append(eval(lls[3]) - eval(lls[4]))
    xl.append(eval(lls[5]))
fi.close()
print(zyc,yyc,xl)
print(jl)

cnt = _________
res = []
res.append(list(("高压最大值", max(jl[1]),max(jl[3]))))
res.append(list(("低压最大值", max(jl[2]),max(jl[4]))))
res.append(list(("压差平均值", )))
res.append(list(("高压平均值", ___________)))
res.append(list(("低压平均值", ___________)))
res.append(list(("心率平均值", ____________)))

# zbg = 0
# ybg = 0
# print('{:<10}{:<10}{:<10}'.format("对比项", "左臂", "右臂"))
# for r in range(len(res) - 1):
#     _____________________
#     ...
#
# if zbg > ybg:
#     print(______________________)
# elif zbg == ybg:
#     print(______________________)
# else:
#     print('______________________)
#     print(', 心率的平均值为{}'.format(res[5][1]))
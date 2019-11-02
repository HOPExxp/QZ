
# from shiyan import elephant




# import numpy as np
# def ave(elements,weights):
#     #需要求加权平均值的数据列表
#     # elements = []
#     #对应的权值列表
#     # weights = []
#     answer = round(sum([j[0]*j[1] for j in zip(elements, weights)])/sum(weights), 1)
#     return answer
# #需要求加权平均值的数据列表
# element = []
# #对应的权值列表
# weight = []
# while True:
#     ele = input('请输入数据：')
#     if ele == '':
#         break
#     element.append(ele)
# while True:
#     wei = input('请输入权值：')
#     if wei == '':
#         break
#     weight.append(wei)
# print(element)
# print(ave(element,weight))

# aliens ={}
# #生成自己想要的外星人
# i = 0
# while True:
#     print('请输入自定义的外星人属性值(name,x_position,y_position)，空格分开:',end=' ')
#     attribute = list(input().split())
#     if attribute:
#         aliens [i]['name'] = attribute[0]
#         aliens [i]['x_position'] = attribute[1]
#         aliens [i]['y_position'] = attribute[2]
#     else:
#         break
#     i += 1


# import socket
# print(socket.gethostname())
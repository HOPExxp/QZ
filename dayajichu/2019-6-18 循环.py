# 作业：
# 1、自己定义一个元祖和一个字典，使用for和while循环遍历里边所有的值
#
# my_tup1 = ('a','b','c','d')
# my_dict1 = {'a':1,'b':2,'c':3,'d':4}
# for tup_value in my_tup1:
#     print(tup_value,end=' ')
#
# 遍历字典时的问题
# for dict_value in my_dict1:
#     print(type(dict_value))  #string类型
#     print(dict_value)    #只能输出字典的键值
#
# 1.分开输出
# for dict_key in my_dict1.keys():
#     print(type(dict_key))
#     print(dict_key)
#
# for dict_value in my_dict1.values():
#     print(dict_value)
#
# 2.利用items方法
# dict_keys = []
# dict_values = []
# for dict_key,dict_value in my_dict1.items():
#     # print('key is '+dict_key)
#     # print('value is '+str(dict_value))
#     dict_keys.append(dict_key)
#     dict_values.append(dict_value)
# print('key is '+str(dict_keys))
# print('value is '+str(dict_values))
#
#
# while
# my_tup1 = ('a','b','c','d')
# my_dict1 = {'a':1,'b':2,'c':3,'d':4}
# i = 0
# while i<len(my_tup1):
#     print(my_tup1[i],end=' ')
#     i+=1
#
# dict_keys = list(my_dict1.keys())
# dict_values = list(my_dict1.values())
# i = 0
# while i<len(my_dict1):
#     print('key is '+dict_keys[i])
#     print('value is ' + str(dict_values[i]))
#     i+=1
#
#
#
# 2、定义两个列表list_a和list_b,判断a中的值再b中有没有，如果有就输出
#
# list_a = ['a','b','c','d']
# list_b = ['c','d','e','f']
# for a_value in list_a:
#     for b_value in list_b:
#         if a_value==b_value:
#             print(a_value)
#         else:
#             pass
#
#
#
# 3、定义两个列表list_a和list_b，把两个列表中对应的位置相加，比如list_a[0]和list_b[0]相加
#
#
# list_a = ['a','b','c','d']
# list_b = ['c','d','e','f','g']
# i = 0
# min_len = min(len(list_b),len(list_a))
# while i<min_len:
#     #多的不能相加
#     print(list_a[i]+list_b[i])
#     i+=1
# #对数多的列表再输出
# else:
#     if len(list_a)>len(list_b):
#         for a_remain in list_a[len(list_b):]:
#             print(a_remain)
#     else:
#         for b_remain in list_b[len(list_a):]:
#             print(b_remain)
#

list = ['a','b']
print(type(list))
for l in list:
    print(type(l))

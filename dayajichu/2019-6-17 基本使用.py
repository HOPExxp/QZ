# 字符串
# 1.单引号，python中基本和双引号作用相同
# str1 = 'my str1'
# 2.双引号，可存储多个字节的字符串
# str2 = "my str2"
# 三引号，多行输出
# str3 = '''
# this is
# my
# str3
# '''
#
# bool类型
# bool1 = True
# bool2 = False
#
# 数字类型
#
# 1.int类型
# int1 = 2
# int2 = -2
#
# 2.float类型
# float1 = 2.1
#
# 3.复数
# complex1 = 1+2j
# print(type(complex1))
#
# 数字类型转化（强制转化）
# int1 = 1
# print(type(float(int1)))
#
# print(type(complex(int1)))
#
# 数字运算
# / 总是返回float类型
# int1 = 5/5
# print(int1)
# // 将浮点数向下取整（int类型）,但是当分子或分母时float类型时，返回float类型
# int2 = 5//2
# int3 = 5//5.0
# print(int2)
# print(int3)
# #
# 数学函数
# import math
# print(abs(-1))  #返回绝对值（int类型）
# print(math.fabs(-1))  #返回绝对值（float类型）
# print(math.ceil(4.1))  #向上取整
# print(math.floor(4.1))  #向下取整
# print(math.exp(1))      #返回e的多少次幂
# print(math.log(math.e))
# print(max('abc'))  #参数为一个序列（字符串、集合、列表、元组）
# print(min('abc'))  #参数为一个序列（字符串、集合、列表、元组）
# print(pow(4,1/2))  #返回x的y次幂,float类型
# print(math.sqrt(4)) #返回平凡根，float类型
# print(round(4.12345,3)) #四舍五入，3表示保留小数位
#
# 列表
# list1 = ['a','b','c','d']
# 下标访问
# print(list1[0])
# print(list1[::-1])  #将列表按-1的步长输出，等效于reverse方法
#
# 1.列表的更新
# list1[0] = 'A'
# print(list1[0])
#
# 2.列表的删除
# 1）del    通过下标删除，或通过全部列表
# del list1[0]
# 2）pop     默认删除列表最后的一个值，可自己添加索引，并且可以赋给一个变量
# pop1 = list1.pop()
# print(pop1)
# 3）remove  通过具体的值删除
# remove1 = list1.remove('c')
# print(list1)
#
# 3.列表的增加值
# 1)列表相加
# list2 = ['e','d']
# print(list1+list2)
# 2）extend方法
# list1.extend(list2)
# print(list1)
# 3)append方法
# list1.append('h')
# print(list1)
# 4)insert方法  在给定索引位置处添加值
# list1.insert(1,'j')
# print(list1)
#
# 4.列表的一些内置函数
# 1）count函数
# print(list1.count('a'))
# 2)index函数
# print(list1.index('A'))
# 3)reverse函数    不能直接print(list1.reverse()),输出None值
# list1.reverse()
# print(list1)
# print(list1.reverse())
# 4）sort函数  同reverse函数
# list1.sort()
# print(list1)
#
# 5.列表的复制  使用[:]将值赋给另一个列表，更改原列表时新列表不会改变
# list2 = list1[:]
# list1[0] = 'a'
# print(list1)
# print(list2)
#
# 元组   tuple  基本和列表相同，不可修改
# tuple1 = ('a','b','c','d')
# try:
#     tuple1[0] = 'A'
#     print(tuple1)
# except:
#     print('元组类型不可改')
#
# 字典类型 dict   一种键值对类型
# dict1 = {str1:'a',str2:'b',str3:'c',}
#
# 字典的更改，通过键对对应的值进行访问并更改其值
# dict1[str1] = 'A'
# print(dict1[str1])
#
# 字符串的删除
# 1）删除指定键所对应的键值对
# del dict1[str1]
# 2）pop 取出键所对应的值，可赋值给其他变量
# value1 = dict1.pop(str1)
# print(value1)
# 3)clear  删除所有键值对
# print(dict1.clear())
#
# 字典的复制  改变原字典时新字典不会改变
# dict2 = dict1.copy()
# print(dict2)
#
# 取字典的键、值、键值对
# print(dict1.keys())
# print(dict1.values())
# print(dict1.items())
#
# 日期类型

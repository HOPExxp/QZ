# 1、定义两种加密方式，再定义list列表，在列表中如果字符串是大写就使用加密方式1，如果是小写就是用加密方式2.

# str_1 = 'abcdefghigklmnopqrstuvwxyz'
# str_3 = '1234567890abcdefghigklmnop'
# str_2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# str_4 = '1234567890ABCDEFGHIJKLMNOP'
# result_1 = str.maketrans(str_1,str_3)
# result_2 = str.maketrans(str_2,str_4)
# list = ['ABCD','abcd','MNOPQ','mnopq','12345','abcd1234','ABCD1234']
# result = []
# false_index = 0
# for i in list:
#     false_index += 1
#     if i.isupper():
#         result.append(i.translate(result_2))
#     elif i.islower():
#         result.append(i.translate(result_1))
#     else:
#         print('第'+str(false_index)+'字符串格式有误')
# print('加密后的列表：'+str(result))


 # 2、定义一个list列表，列表中字符串是大写字母开头的放到L_1中，如果是以”dfs”结尾的放在L_2中。比较L_1和L_2的长度，要求最后输出结果两个列表长度相等。

list = ['Abcd','abdfs','Bsgsdfs','AEF']
L_1 = []
L_2 = []
for i in list:
    if i[0].isupper():
        L_1.append(i)
    #两个条件均符合时会出错
    # elif i.endswith('dfs'):
    #     L_2.append(i)
for j in list:
    if j.endswith('dfs'):
        L_2.append(j)
min_len = min(len(L_1),len(L_2))
if len(L_1) == len(L_2):
    print('两个列表长度相等，结果为：')
    print('L_1:' + str(L_1))
    print('L_2:' + str(L_2))
else:
    print('两个列表长度不等,调整结果为：')
    print('L_1:' + str(L_1[:min_len]))
    print('L_2:' + str(L_2[:min_len]))
# 作业：
# 1、定义一个字符串列表，统计出多少个全部大写字符串，多少个全部小写的字符串，多少个纯字母的字符串

string_list = ['abcd','ABCD','aB  cd','AB  12']
lower_num = 0
upper_num = 0
alpha_num = 0
for i in string_list:
    if i.islower() :
        # if i.isalnum():
        #     continue
        # else:
        print(i)
        lower_num += 1
print('全部是小写的字符串数：' + str(lower_num))

for i in string_list:
    if i.isupper():
        # if i.isalnum():
        #     continue
        # else:
        print(i)
        upper_num += 1
print('全部是大写的字符串数：'+str(upper_num))

# string = 'ab123'
# print(string.islower())
# print(string.isupper())
#islower()、isupper()方法只对字符串中可区分大小写的字符进行判断，若无可判断大小写的字符则返回False
#不能判断空格、数字
#可遍历字符串将空格、数字等删除
#可遍历字符串判断是否存在空格、数字等

for i in string_list:
    if i.isalpha():
        print(i)
        alpha_num += 1
print('是纯字母的字符串数：'+str(alpha_num))

# 2、定义一个字符串列表，把所有的小写字母组成的字符串累加在一起

string_list = ['abcd','ABCD','ab  cd','AB  12']
lower_string = ''
for i in string_list:
    if i.islower():
        lower_string += i
print('小写字符串累加值：'+lower_string)

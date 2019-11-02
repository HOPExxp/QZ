# 1、定义一个空的list和一个空的set，一个不可变的set。
# 2、输入5个字符串给list：
# 3、如果list中的值不是”error”就都添加在set中
# 4、把不可变的set的值都放到set中。
# 5、判断可变集合和不可变集合的关系是不是issubset。如果是输出YES

li = []
jh1 = set()
jh2 = frozenset('I LOVE PYTHON')
while len(li)<5:
    l = input('请输入字符串：')
    li.append(l)
# print(li)

for value in li:
    if value != 'error':
        jh1.add(value)
    else:
        continue

jh1.update(jh2)
# print(jh1)
# print(jh2)
if jh2.issubset(jh1):
    print('YES')
else:
    pass

# jh2 = frozenset('I,LOVE,PYTHON')  #不可变集合中只允许有一个元素

# print(jh2)
# jh=frozenset('s','d')
# print(jh)

# jh2=set(['a','d'])   #set函数中只能为 组合数据类型 或 不可变集合
# jh1={'a','s'}
# print(jh2)

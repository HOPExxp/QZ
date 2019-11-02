#操作类函数
import json
#解析类函数

#python数据类型
dt = {'b':2,'c':4,'a':6}

#转换为json格式数据
s1 = json.dumps(dt,)

#对key值进行排序，每个数据前缩进4个单位
s2 = json.dumps(dt,sort_keys=True,indent=4)

print(s1)
print(s2)
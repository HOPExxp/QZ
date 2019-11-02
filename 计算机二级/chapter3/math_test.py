#math库提供四种数学常数和44个函数
#44个函数又分为4类：16个数值表示函数，8个幂对数函数，16个三角对数函数，4个高等特殊函数


import math

# #4个数学常数
# print(math.pi)
# print(math.e)
# print(math.inf)  #正无穷
# print(math.nan)  #非浮点数标记


# #16个数值表示函数
# print(math.fabs(-2))                #取绝对值
# print(math.fmod(5,3))               #返回x与y的模   5%3=2
# print(math.fsum([1.0,1.34,4.32]))   #返回浮点数的精确求和       **********处理浮点数时，最好使用math提供的函数，运算符会有误差
# print(math.ceil(5.3))               #向上取整  -->6
# print(math.floor(5.3))              #向下取整  -->5
# print(math.factorial(4))            #返回x的阶乘                ----------x为负数或小数时，返回一个valueerror错误
# print(math.gcd(8,24))               #返回x、y的最大公约数
# print(math.modf(3.4))               #返回x的小数和整数部分，元组形式
# print(math.trunc(3.4))              #返回x的整数部分
# print(math.copysign(3,-1))          #用y的符号替换x的符号


# #8个幂对数函数
# print(math.pow(2,3))                  #返回x的y次幂
# print(math.exp(2))                    #返回e的x次幂
# print(math.expm1(2))                  #返回e的x次幂减一
# print(math.sqrt(4))                   #返回x的平方根
#
# print(math.log(8,2))                  #返回log2（8） -->3
# print(math.log1p(math.e-1))           #返回1+x的自然对数值   ln(x+1)
# print(math.log2(4))                   #返回以2为底的对数值   log2（x）
# print(math.log10(100))                #返回以10为底的对数值  log10（x）


#16个三角运算函数
print(math.degrees(math.pi))          #角度的弧度值转角度值
print(math.radians(180))              #角度的角度值转弧度值

#4个高等特殊函数
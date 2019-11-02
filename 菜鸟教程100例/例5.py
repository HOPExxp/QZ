# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。
#
# 程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。

a = int(input('请输入第一个值：'))
b = int(input('请输入第二个值：'))
c = int(input('请输入第三个值：'))
# if a < b:
#     if b < c:
#         print(str(a),str(b),str(c))
#     elif c < b:
#         if a < c:
#             print(str(a),str(c),str(b))
#         else:
#             print(str(c),str(a),str(b))
#无论怎样都输出abc


#加大难度：一直输入数字，每次输入完从小到大输出全部值


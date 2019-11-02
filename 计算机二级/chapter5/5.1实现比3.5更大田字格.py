

# a , b , c , d = '-','+','|',' '
# # n = int(input('阶数>>'))
# n = 4
# for i in range(1,n*4 + 5 + 1):
#     if i % 5 == 1:
#         #  ******  此种格式化适用于知道固定的阶数
#         print('{0}{1}{0}{1}{0}{1}{0}{1}{0}'.format(b,a*4))
#     else:
#         print('{0}{1}{0}{1}{0}{1}{0}{1}{0}'.format(c,d*4))

#函数版
def tian(jie,gap):
    #jie  阶数  ；  gap  间隔
    a, b, c, d = '-', '+', '|', ' '
    for i in range(1,jie*gap + jie + 1 + 1):
        if i % (gap+ 1)== 1:
            # print('{0}{1}{0}{1}{0}{1}{0}{1}{0}'.format(b, a * 4))
            for j in range(jie):
                print('{}{}'.format(b,a*gap),end='')
            print(b)
        else:
            # print('{0}{1}{0}{1}{0}{1}{0}{1}{0}'.format(c, d * 4))
            for j in range(jie):
                print('{}{}'.format(c,d*gap),end='')
            print(c)
tian(5,4)







#网上参考版
# n = eval(input('请输入一个奇数：'))
#
# a = '-'
#
# b = '+'
#
# c = '|'
#
# d = " "
#
# m = n // 2
#
# for i in range(n):
#
#     if i in [0, m, n - 1]:
#
#         print("{0}{1}{0}{1}{0}".format(b, a * (m - 1)))
#
#     else:
#
#         print("{0}{1}{0}{1}{0}".format(c, d * (m - 1)))
#
#
# #        **************** 2 *********
# def drawsq(n):
#     line=3*n+1
#     for i in range(1,line+1):
#         if i%3 ==1:
#             print(n*"+----",end="")
#             print("+")
#         else:
#             print ("|    "*n,end="")
#             print("|")
#
# def main():
#     n=eval(input("请输入您想要的阶数："))
#     drawsq(n)
#
# main()


# ls1 = [12,0,0,2]
# # Return True if bool(x) is True,for any x in the iterable.
# # If the iterable is empty, return False
# print(all(ls1),any(ls1))


#操作题1
# s = input()
# print("{:=>25,d}".format(eval(s)))

# ls= input()
# ls = ls.split(",")
# print("{0}{1}{0}".format(ls[1]*int(ls[0]),str(ls[0])))
# print("{0}{1}{0}".format("a","b"))

#操作题6
# picd = {}
#
# fi = open("dir_50.txt",'r')
# for l in fi:
#     l=l.replace('\n','').split('_')
#     # print(l[1])
#     lkey = l[1].split(".")[0]
#     lv = eval(l[0])
#     for i in range(lv.count("0")):
#         lv.remove("0")
#     # print("{}:{}".format( lkey,lv))
#     picd[lkey] = lv
# fi.close()
# print(picd)
#
# idd = {}
# for key in picd:
#     for k in picd[key]:
#         idd[k] = idd.get(k,1) + 1
#     #print(num,idd[num])
# print(idd)
#
# s = 0
# for key in idd:
#     s += idd[key]
#     # print("{}:{}".format(key, idd[key]))
# count = len(idd)
# print("实际参加测试的人数是：",count)
# print("人均被测次数是：{:.1f}".format(s/count))


#操作2
# import turtle
# turtle.pensize(2)
# d=0
# for i in range(1,13):
#     turtle.fd(40)
#     d += 30
#     turtle.seth(d)
# turtle.done()
# print("13")
# print("turtle.fd(40)")
# print("30")

#22
# for i in range(3):
#
#     if i == 2:
#
#         print('found it! i =', i)
#
# else:
#
#     print('not found it ...')

#24
# try:
#
#     a,b=eval(input("请输入2个整数，用逗号隔开："))
#
# except:
#
#     print('请重新输入')
#
# print(a/b)

#30
# h,w=eval(input("请输入2个整数，用逗号隔开："))
#
# k = h//w
#
# print(k,type(k))

#34
# fo = open("text.csv",'w',encoding="utf-8")

x = ["90,85,70"]

print(",".join(x))

# fo.write(",".join(x))
#
# fo.close()
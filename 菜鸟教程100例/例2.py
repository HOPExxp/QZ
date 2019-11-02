#coding:utf-8
# 题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部#10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提#成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应#发放奖金总数？
# 程序分析：请利用数轴来分界，定位。注意定义时需把奖金定义成 长整型
#最基本的思路
jj = 0
lirun = eval(input('请输入当月利润(万元)：'))
if lirun>=0 and lirun<10:
    jj = lirun * 0.1
elif lirun>=10 and lirun<20:
    jj = 10*0.1 + 0.075*(lirun - 10)
elif lirun>=20 and lirun<40:
    jj = 10*0.1 + 10*0.075 + 0.05*(lirun-20)
elif lirun>=40 and lirun<60:
    jj = 10*0.1 + 10*0.075 + 20*0.05 + 0.03*(lirun-40)
elif lirun>=60 and lirun<100:
    jj = 10*0.1 + 10*0.075 + 20*0.05 + 20*0.03 + 0.015*(lirun-60)
elif lirun>=100:
    jj = 10*0.1 + 10*0.075 + 20*0.05 + 20*0.03 + 40*0.015 +0.01*(lirun-100)
else:
    print('利润值为负')
print('所得奖金为：' + str(jj))
# 题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部#10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提#成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应#发放奖金总数？
# 程序分析：请利用数轴来分界，定位。注意定义时需把奖金定义成 长整型
i = int(input('请输入实际利润：（元）'))
#细节：从大到小
arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
#用来存储结果
r = 0
for idx in range(0,6):
    if i > arr[idx]:
        r += (i-arr[idx])*rat[idx]
        print ((i-arr[idx])*rat[idx])
        i=arr[idx]
print(r)

#############################   2019-7-10~11
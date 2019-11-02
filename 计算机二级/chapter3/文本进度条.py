# #e4.1TextProgress Bar.py
# import time
# scale = 20
# print("------执行开始------")
# for i in range(scale+1):
#     a, b = '**' * i,'..' * (scale - i)
#     c = (i/scale)*100
#     #\r  下一次print时会将指针移动到行首，即实现了覆盖功能
#     print("\r%{:>3.0f}[{}->{}]" .format (c, a, b),end='')
#     time.sleep(0.1)
# print("\n------执行结束------")



#带刷新的文本进度条
#time.clock实现时间的监控
import time
scale = 50
print('执行开始'.center(scale//2,'-'))
#设置时间的初始值
t1 = time.time()
# print(t)
for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i/scale)*100
    t2 = time.time()
    t = t2 -t1
    # t = time.clock() - t
    print('\r%{:>3} [{}->{}] {:<3}s'.format(c,a,b,t),end='')
    time.sleep(0.05)
print('\n'+'执行结束'.center(scale//2,'-'))

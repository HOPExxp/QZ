#打印格式：  Starting ··· Done！
import time
scale = 50
for i in range(scale+1):
    a = '·' * i
    print('\rStarting{:<50}'.format(a),end='')
    time.sleep(0.05)
print('Done!')
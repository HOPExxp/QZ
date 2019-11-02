#一年365天，以第一天的能力值为基数，记为1.0.当好好学习时能力值相比前一天高0.1%，当没有好好学习时能力值相比前一天低0.1%。
# 每天学习与每天放任一年后的能力值相差多少呢

import math
yearup = math.pow(1.01,365)
# yeardown = math.pow(0.99,365)
# print('学习：{:.2f}，放任：{:.2f}'.format(yearup,yeardown))


#工作日提升1%，周末放任1%
# import math
# standand,dayfactor = 1.0,0.01
# for i in range(365):
#     if i%7 in [6,0]:
#         standand *= (1-dayfactor)
#     else:
#         standand *= (1+dayfactor)
# print('工作日提升1%，周末放任1%:{:.2f}'.format(standand))

#周末放任，工作日得多努力才能达到每天提升1%的功效
import math
def dayUp(dayfactor):
    standand = 1.0
    for i in range(365):
        if i%7 in [6,0]:
            standand *= (1-0.01)
        else:
            standand *= (1+dayfactor)
    return standand
dayfactor = 0.01
while dayUp(dayfactor)<yearup:
    dayfactor += 0.001
print('周末放任，工作日得多努力才能达到每天提升1%的功效:{:.3f}'.format(dayfactor))
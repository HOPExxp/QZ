# 模拟定义一个汽车列表，列表中需要针对每种车型列出五个必要的参数说明：
# 比如  byd  （耗油 100，车长 5 ，车高 2 ，轮胎 4，单价  1万）等。
# 对于不同车型要求提价，要求每种车型，油耗是100以上的，就把单价增加1000元。

cars_list = []
car1 = {'name':'大众',
        'attribute':
            {'consume':100,'car_length':5,'car_heigth':2.5,'tire':4,'price':15000}
        }
car2 = {'name':'五菱',
        'attribute':
            {'consume':120,'car_length':5,'car_heigth':2,'tire':4,'price':10000}
        }
car3 = {'name':'奔驰',
        'attribute':
            {'consume':80,'car_length':4.5,'car_heigth':2,'tire':5,'price':20000}
        }
cars = [car1,car2,car3]
for car in cars:
    if car['attribute']['consume'] >= 100:
        car['attribute']['price'] += 1000
    print(car)


# 模拟消灭外星人的游戏
# 只做一个外星人字典列表—三个字段（名称，x坐标，y坐标），在只做一个要杀死的外形人的坐标，如果坐标匹配，就删除这个外星人

#生成一个外星人列表，每个外星人都相同
alien_length = input('请输入外星人的数量：')
aliens = []
for i in range(int(alien_length)):
    start_alien = {'name': '甲', 'x_position': 3, 'y_position': 4}
    aliens.append(start_alien)

# #生成自己想要的外星人
# i = 0
# while True:
#     alien_attribute = input('请输入自定义的外星人属性值(name,x_position,y_position)，空格分开:')
#     if alien_attribute == '':
#         break
#     attribute = list(alien_attribute)
#     aliens [i]['name'] = attribute[0]
#     aliens [i]['x_position'] = attribute[2]
#     aliens [i]['y_position'] = attribute[4]
#     i += 1
#生成自己想要的外星人
i = 0
while True:
    print('请输入自定义的外星人属性值(name,x_position,y_position)，空格分开:',end=' ')
    attribute = list(input().split())
    if attribute:
        aliens [i]['name'] = attribute[0]
        aliens [i]['x_position'] = attribute[1]
        aliens [i]['y_position'] = attribute[2]
    else:
        break
    i += 1


kill_list = []
while True:
    #生成想要杀死的外星人坐标列表
    print('请输入你想kill的外星人坐标(x_position,y_position):',end=' ')
    kill = list(input().split())
    if kill:
        kill_list.append(kill)
    else:
        break

try:
    # 删除匹配成功的外星人
    copy_aliens = aliens.copy()
    for alien in aliens:
        i = 0
        for one in kill_list:
            if int(alien['x_position']) == int(one[0]) and int(alien['y_position']) == int(one[1]):
                # del aliens[i]
                # print('杀死的外星人为：'+str(aliens[i]))
                print('杀死的外星人为：' + str(alien))
                del copy_aliens[i]
        i += 1

    print('存活的外星人为：' + str(copy_aliens))
except:
    print('kill数大于外星人数')


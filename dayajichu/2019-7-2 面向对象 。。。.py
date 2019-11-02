# 写一个类：能够实现一个非常大的过程，从深圳到北京（出租，飞机，骑单车，走路）
# 通用性非常强的类：同一个一个北京到深圳的过程，达到所有的人都可以使用这个类出行。
class Out():
    # means = {'1':'self.taxi()','2':'self.plane()','3':'self.bike()','4':'self.walk()'}
    def __init__(self,sta_station,fin_station):
        self.sta_station = sta_station
        self.fin_station = fin_station
        my_choice = list(input('请输入你出行的方式：({1:taxi,2:plane,3:bike,4:walk)'))
        # for choice in my_choice:
        #     print(choice)
        #     self.(Out.means[choice])
        for choice in my_choice:
            if choice == '1':
                _1 = input('请输入出发地：')
                _2 = input('请输入目标地：')
                self.taxi(_1._2)
            elif choice == '2':
                self.plane()
            elif choice == '3':
                self.bike()
            elif choice == '4':
                self.walk()
            else:
                print('没有' + choice + '所对应的出行方式')

    def taxi(self,start,end):
        print('从 ' + start + ' 坐出租车去 ' + end)

    def plane(self):
        print('从 ' + self.sta_station + ' 坐飞机去 ' + self.fin_station)

    def bike(self):
        print('从 ' + self.sta_station + ' 骑单车去 ' + self.fin_station)

    def walk(self):
        print('从 ' + self.sta_station + ' 走路去 ' + self.fin_station)

out1 = Out('深圳','北京')

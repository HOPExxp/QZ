# 定义父类和母类，分别定义不同的参数和方法
# 1、实现一个子类，继承父类和母类的所有方法，并且重写一个父类的方法
# 2、在子类中实现一个私有变量和私有方法，并且定义一个出口的方法改变私有变量的值，在提供一个私有方法的出口。

class Student():
    def __init__(self,name,xuehao,zhuanye):
        self.name = name
        self.xuehao = xuehao
        self.zhuanye = zhuanye
    def study(self):
        print(self.name + ' like study')

class Worker():
    def __init__(self,gongzhong,):
        self.gongzhong = gongzhong
    def work(self):
        print( ' like work')
    def discribe_work(self):
        print('name:' +  'gongzhong:' + self.gongzhong)

class StuWork(Student,Worker):
    def __init__(self,name,xuehao,zhuanye,gongzhong,hobby):
        Student.__init__(self,name,xuehao,zhuanye)
        Worker.__init__(self,gongzhong)
        self.__name = name
        self.__hobby = hobby
        self.__xuehao = xuehao
    def study(self):
        print(self.name + ' like study,also like work')
    def work(self):
        print(self.name + ' like work,also like study')
    # #私有属性的出口
    # @property
    # def xh(self):
    #     return self.__xuehao
    # @xh.setter
    # def xh(self,change):
    #     self.__xuehao = change
    #私有方法
    def __discribe_stu(self):
        print('name:' + self.name + 'xuehao:' + self.__xuehao + 'zhuanye:' + self.zhuanye)
    #私有方法的出口
    def discribe(self):
        self.__discribe_stu()

pers = StuWork('小明',6000111105,'计算机','实习','玩游戏')
print(pers.xuehao)
print(pers.name)
# print(pers.hobby)
pers.study()
pers.work()
print(pers.xuehao)
pers.xh = 6003111105
print(pers.xuehao)
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
    def __init__(self,name,gongzhong,):
        self.name = name
        self.gongzhong = gongzhong
    def work(self):
        print(self.name + ' like work')
    # def discribe_work(self):
    #     print('name:' + self.name + 'gongzhong:' + self.gongzhong)

class StuWork(Student,Worker):
    #两个字类中均有name属性会有影响吗？
    def __init__(self,name,xuehao,zhuanye,gongzhong,hobby):
        Student.__init__(self,name,xuehao,zhuanye)
        Worker.__init__(self,name,gongzhong)
        #子类不能隐藏父类属性？
        # self.__name = name
        # self.__xuehao = xuehao
        #私有属性
        self.__hobby = hobby
    #私有属性的改变及出口
    @property
    def xh(self):
        return self.__hobby
    @xh.setter
    def xh(self,change):
        self.__hobby = change
    #私有方法
    def __discribe_stu(self):
        print('name:' + self.name + ' xuehao:' + str(self.xuehao) + ' zhuanye:' + self.zhuanye)
    #私有方法的出口
    def discribe(self):
        self.__discribe_stu()
    #重写两个方法
    def study(self):
        print(self.name + ' like study,also like work')
    def work(self):
        print(self.name + ' like work,also like study')

pers = StuWork('小明',6000111105,'计算机','实习','玩游戏')
# print(pers.xuehao)
# print(pers.name)
# print(pers.hobby)

print('-----私有属性输出结果-----')
#注意调用格式
pers.xh = '看书'
print(pers.xh)
print('-----重写方法结果-----')
pers.study()
pers.work()
print('-----私有方法结果-----')
pers.discribe()
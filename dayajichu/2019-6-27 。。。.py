# 写一个小狗出生的过程，并且计算出生了多少个小狗，再写一个狗狗吃奶的过程，小狗可以主动吃奶，也可以狗妈妈喂小狗。
# 提示：1、不断有新的小狗对象产生，不断累积数量，最后累积结果就是小狗的数量。
#       2、狗狗吃奶的过程只需要一个比较特殊的函数就能解决

##用@classmethod方法或staticmethod方法定义drinkMilk函数

import random
class Dog():
    count = 0
    def __init__(self,name='huahua'):
        Dog.count += 1
        self.name = name
        self.喝奶量 = 0
    #调用时用False则妈妈喂，每次喂一份；用True则自己喝奶,每次喝的量都不同，但大于妈妈喂的量
    def drinkMilk(self,wei=False):
        if wei == False:
            print('妈妈不喂我喝奶，那我就自己喝吧')
            self.喝奶量 = round(random.uniform(0.5,1,) * 2,2)
            print('喝奶量：' + str(self.喝奶量))
        else:
            print('妈妈最好啦，知道我饿了喂我奶喝')
            self.喝奶量 = 1
            print('喝奶量：' + str(self.喝奶量))
    def __str__(self):
        return str(self.喝奶量)

my_dog1 = Dog('heihei')
my_dog2 = Dog('baibai')
my_dog3 = Dog('feifei')
my_dog4 = Dog('meimei')
print(Dog.count)
my_dog1.drinkMilk(False)
my_dog2.drinkMilk(True)

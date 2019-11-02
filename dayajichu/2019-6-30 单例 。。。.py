# 1、定义两个类，里边的方法名完全一样，但是内容不相同，在使用这种多态性质的时候，要求一次性调用两个类的两个不同方法：比如   A类（a,b）,B类（a,b）,同时调用A.a,B.b。
# 2、用任何一种方式在把A,B改成单例模型，最简单的方式，不需要考虑多线程
class Dog(object):
    # b = 1
    def __init__(self,name):
        self.name = name
        # Dog.b += 1
        # print(Dog.b)
    def run(self):
        print(self.name + ' can run')
    def eat(self):
        print(self.name + ' can eat')
    #单例方法一：函数方法
    def __new__(cls, *args, **kwargs):
        #hasattr方法：判断一个对象是否包含某个属性（用字符串表示 ——’属性名’）
        if not hasattr(Dog,'instance'):
            Dog.instance = object.__new__(cls)
            # Dog.b += 1
            # print(Dog.b)
        return Dog.instance

#单例方法二：修饰器
def Singleton(cls):
    _instance = {}
    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]
    return _singleton
@Singleton
class Cat():
    # a = 1
    def __init__(self,name):
        self.name = name
        # Cat.a += 1
        # print(Cat.a)
    def run(self):
        print(self.name + ' can run very fast')
    def eat(self):
        print(self.name + ' eat fish')

def see(animal):
    animal[0].run()
    animal[1].eat()




#实例化的是对象对类的属性无影响，属性值可以改变
#使用__new__ 内置函数方法可以再次实例化，但是之前所有的实例均变为最新实例的那个，即用最后实例的那个
dog1 = Dog('huahua')
dog2 = Dog('feifei')
print(dog1,dog2)
print(dog1.name,dog2.name)
#使用修饰器方法不能再次实例化，之后所有的实例均变为最开始实例的那个，即用最开始实例的那个
cat1 = Cat('heihei')
cat2 = Cat('beibei')
print(cat1,cat2)
print(cat1.name,cat2.name)

#一次调用两个实例的不同方法
animals = [dog1,cat1]
see(animals)
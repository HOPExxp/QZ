
# 写一个大象，所有的大象在一生下来都是有长长的鼻子，粗糙的皮肤，并且可以呼吸的。把这些特性描述出来（一产生就有这些。），并且大象是由年龄，和名字的。
# 定义大象吃草的方法，吃草大象就长大，每次1吨长30斤。当年龄是5岁的时候停止生长。

class elephant():
    #默认值表示刚出生的小象体重约为100
    def __init__(self,name,age=0,weight=100):
        self.name = name
        self.age = age
        if self.age < 0:
            print('*年龄不能为负数，请仔细检查*')
        self.weight = weight
        print('----------------------')
        print('下面是小象的基本特征')
        print(self.name + ' have long nose')
        print(self.name + ' have rough skin')
        print(self.name + ' can breath')
        print('----------------------')

    #吃草长大，每吃1吨长30斤
    def eat_grass(self,num):
        if self.age < 5:
            self.weight += 30 * num
        else:
            print('小象已经长大，不能再长身体啦')

    # #老师 ， 自己瞎写的,可以不用看
    # #年龄增长，和体重有一定的联系，假设长200斤左右增加1岁
    # def age_growth(self):
    #     #吃草值拿不过来
    #     self.age +=

    #运行完程序自动输出小象的基本信息
    def __del__(self):
        print('*********************')
        print('名字：' + self.name + ' 年龄：' + str(self.age) + ' 重量：' + str(self.weight))

my_ele = elephant('huahua',5)
# my_ele.eat_grass(3)



# #花花  eat  drink  sleep  --对象     由类产生--对象
# # 区别---     init   为什么？？
# # 执行的先后顺序，在初始化的时候init和del就执行了
#
# # 其他的所有的方法，是在调用的时候才执行，不调用不执行
# class Dog:
#     def __init__(self,name,age):
#         self.name = name + "name"
#         self.age = age + 10
#         print('hello')
#     def eat(self):
#         print(self.name+"Eat")
#     def drink(self):
#         print("Drink")
#     def sleep(self):
#         print("Sleep")
#     def __del__(self):
#         print(self.name+"--",self.age+10)
# huahua = Dog("huahua",10)
# huahua.eat()
# huahua.drink()

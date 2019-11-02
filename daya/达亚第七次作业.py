# 定义一个类-类名为Cat，添加两个属性，name和age
# 分别定义：吃、跑的函数，要求每个年龄段的猫吃的量都不一样（0-1岁：3,1-4岁：8,5-10:5），每个年龄段跑的长度不同：（0-1岁：0.1,1-4岁：0.3,5-10:0.2）
# 调用三个不同年龄段的猫
#
# 定义一个类飞机
# 类中定义描述的函数，描述飞机的所有性质，型号+大小+年限
# 书写一个读取飞机公里数的函数
# 书写一个飞机每天运行公里数增加的函数
# 书写一个飞机报废的函数，当公里数超过100万就报废，输出飞机报废了


class plane():
    def __init__(self,type,size,age):
        self.type = type
        self.size = size
        self.age = age

    #def get_miles(self):





#class Cat():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def eat(self):
#         if self.age==0 or self.age==1:
#             return 3
#         if self.age==2 or self.age==3 or self.age==4:
#             return 8
#         if self.age==5 or self.age==6 or self.age==7 or self.age==8 or self.age==9 or self.age==10:
#             return 5
#     def run(self):
#         if self.age==0 or self.age==1:
#             return 0.1
#         if self.age==2 or self.age==3 or self.age==4:
#             return 0.3
#         if self.age==5 or self.age==6 or self.age==7 or self.age==8 or self.age==9 or self.age==10:
#             return 0.2
# my_cat1 = Cat('tom',1)
# my_cat2 = Cat('jerry',4)
# my_cat3 = Cat('mike',8)
# print(my_cat1.name+' can eat '+str(my_cat1.eat())+','+'its age is '+str(my_cat1.age))
# print(my_cat1.name+' can eat '+str(my_cat1.run())+','+'its age is '+str(my_cat1.age))
# print(my_cat2.name+' can eat '+str(my_cat2.eat())+','+'its age is '+str(my_cat2.age))
# print(my_cat2.name+' can eat '+str(my_cat2.run())+','+'its age is '+str(my_cat2.age))
# print(my_cat3.name+' can eat '+str(my_cat3.eat())+','+'its age is '+str(my_cat3.age))
# print(my_cat3.name+' can eat '+str(my_cat3.run())+','+'its age is '+str(my_cat3.age))
#
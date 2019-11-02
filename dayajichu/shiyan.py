# class elephant():
#     #默认值表示刚出生的小象体重约为100
#     def __init__(self,name,age=0):
#         self.name = name
#         self.age = age
#     def print(self):
#         print('name:'+self.name+' age:'+str(self.age))
#
# class abc(elephant):
#     def __init__(self,name,age,ooo):
#         self.name = name
#         self.age = age
#         self.ooo = ooo
#         super().__init__(name,ooo)
#     def print1(self):
#         print('name:'+self.name+' age:'+str(self.age))
#
# a = abc('huahua',20,'fsf')
# a.print()
# a.print1()
#
# my_choice = list(input('请输入你出行的方式：(1:taxi,2:plane,3:bike,4:walk)'))
# print(my_choice)

list = ['Abcd','abdfs','Bsgsdfs','AEF']
for i in list:
    print(i)
    i = 'a'
    print(i)
print(list)

#逻辑运算符
# a = 0
# b = 0
# print(a and b)
# print(a or b)
# print(not b)

#位运算符
# a = 60
# print(bin(a))
# print(bin(~a))
# print(a)
# print(~a)
# #取反加一再取反
# b = -60
# print(bin(b))
# print(bin(~b))
# print(b)
# print(~b)


# def print_models(unprinted_designs, completed_models):
#   while unprinted_designs:
#    current_design = unprinted_designs.pop()
#    print("Printing model: " + current_design)
#    completed_models.append(current_design)
# def show_completed_models(completed_models):
#   print("\nThe following models have been printed:")
#   for completed_model in completed_models:
#    print(completed_model)
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)
# print(unprinted_designs)

#5、用面上对象的思想写一个开枪打仗的过程（装弹，瞄准，射击）

# def zhuandan(num):
#     bullet_num = 0
#     bullet_num += num
#     print('剩余子弹数为：' + str(bullet_num))
#     return bullet_num
# def miaozhun(target):
#     print('已瞄准目标'+target)
#     return  target
# def sheji(bullet_num,target):
#     bullet_num -= 1
#     print('恭喜你，射中了' + target)
#     print('剩余子弹数为：' + str((bullet_num )))
# num = zhuandan(3)
# target = miaozhun('Tom')
# sheji(num,target)

# 6、写一个关于手机的函数，每个手机都可以打电话、发短信、发视频等。定义一个私有的品牌属性，并且定义一个出口来让别人使用。
# class phone():
#     def __init__(self,pingpai,name):
#         self.__pingpai = pingpai
#         self.name = name
#         print('my ' + self.name + ' phone can 打电话' )
#         print('my ' + self.name + ' phone can 发短信')
#         print('my ' + self.name + ' phone can 发视频')
#     def get_pingpai(self):
#         print('my phone pingpai is ' + self.__pingpai)
# myph = phone('小米','小艾')
# myph.get_pingpai()

# 7、定义两个类，A为父类，B为子类，给A定义一个私有方法，并且提供一个B来继承的方式。
# class A ():
#     def __init__(self,father):
#         self.father = father
#     def __own(self):
#         print('这是一个私有方法')
#     def own_out(self):
#         self.__own()
# class B(A):
#     def __init__(self,father):
#         A.__init__(self,father)
#         self.own_out()
# b = B('father')

#9
# class Open_File():
#     filename = 'pi_digits.txt'
#     def __init__(self,____= 'pi_digits.txt'):
#         self.____ = Open_File().filename
#     def open(self,_____= 'pi_digits.txt'):
#       with open(Open_File().filename) as file_object:
#        lines = file_object.______()
#        pi_string = ''
#        for line in lines:
#           pi_string += line.____()+"\n"
#        print(pi_string.____())
# pi_string = Open_File()
# ll =pi_string.open()

#10
def count_words(filename):
  """ 计算一个文件大致包含多少个单词 """
  try:
      with open(filename) as f_s:
          cons = f_s.read()
      num_words = 0
      for i in cons:
          num_words+=1
  except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
  else:
# 计算文件大致包含多少个单词

    print("The file " + filename + " has about " + str(num_words) +" words.")
filename = 'programming.txt'
count_words(filename)
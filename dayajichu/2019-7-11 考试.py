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


# 8、用get和set函数实现一个私有变量被设置和取值的一个过程。
# class dog():
#     def __init__(self,name,age):
#         self.name = name
#         self.__age = age
#     def get(self):
#         return self.__age
#     def set(self,change):
#         self.__age = change


# 9、把下面的程序填完整:
# class Open_File():
#     def __init__(self,filename= 'shiyan.txt'):
#         self.filename = filename
#     def open(self,filename= 'shiyan.txt'):
#       with open(filename) as file_object:
#        #read:读取所有内容，相当于原封不动的输出，一整个长字符串；readline:输出第一行的所有内容；readlines:以每行作为一个元素，存储再一个列表中
#        lines = file_object.readlines()
#        # print(lines)
#        pi_string = ''
#        for line in lines:
#           # print(line)
#           pi_string += line.strip()+"\n"
#        print(pi_string.strip())
# pi_string = Open_File()
# ll =pi_string.open()

# 10、把下列程序的确实部分书写完整：
def count_words(filename):
    """ 计算一个文件大致包含多少个单词 """
    try:
        with open(filename) as f:
            fl = f.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
    # 计算文件大致包含多少个单词
    #split:默认所有空字符均分割  splitlines:默认\r \n \ r\n
        fll = fl.splitlines()
        num_words = len(fll)
    print("The file " + filename + " has about " + str(num_words) +" words.")
filename = 'shiyan.txt'
count_words(filename)
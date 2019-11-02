#文件的操作，文件的写操作、open有三种打开方式,r-w-a,默认就是r-只能读，w--写的方式,
# a--叫做附加方式，进行文件的追歼,
# 添加文件内容的方式---有文件直接添加---没文件当前目录创建
class File1():
    def __init__(self,filename):
        self.filename = filename
        with open(self.filename,'a') as file1:
            for i in range(100):
                file1.write("I am a Daya teacher,my Class have 14 students."+"\n")

# file1 =File1('data.txt')

class XunHuan():
    def __init__(self):
        while True:
            i = input("i:")
            j = input("j:")
            try:
                res = int(i)/int(j)
            except ZeroDivisionError:
                print("Can not input 0 to j")
            except:
                print('没给值')
                break
            else:
                print(res)

xh = XunHuan()

# #不会因为文件不存在导致整个的对外响应终止
class File2():
    def __init__(self,filename):
        self.filename = filename
        try:
            with open(self.filename) as f_s:
                cons = f_s.read()
        except FileNotFoundError:
            log = "Your file:"+self.filename + " not exist. "
            print(log)
        else:
            print(cons.splitlines())
            print(len(cons.splitlines()))

file2 = File2('data.txt')
file2_ = File2('aaa.txt')


# #不会因为文件不存在导致整个的对外响应终止
class File3():
    def __init__(self,filename):
        self.filename = filename
        try:
            with open(self.filename) as f_s:
                cons = f_s.read()
        except :
            log = "Your file:"+self.filename + " not exist. "
            print(log)
        else:
            lines = cons.splitlines()
            print(len(lines))
            print(self.filename + " is right : the file has words:" + str(len(lines)))
        finally:
            print("恭喜你完成了")

file3 = File3('data.txt')
file3_ = File3('aaa.txt')

# #不会因为文件不存在导致整个的对外响应终止 1,2,3,4
class File4():
    def __init__(self,filename):
        self.filename = filename
        try:
            with open(self.filename) as f_s:
                cons = f_s.read()
        except FileNotFoundError:
            log = "Your file:"+self.filename + "not exist. "
            print(log)
        except FileExistsError:
            log = "Your file:"+self.filename + "is exist. "
            print(log)
        else:
            lines = cons.splitlines()
            print(len(lines))
            print(self.filename + " is right : the file has words:" + str(len(lines)))
        finally:
            print("恭喜你完成了")

file4 = File4('data.txt')
file4_ = File4('aaa.txt')

# #不会因为文件不存在导致整个的对外响应终止 1,2,3,4
class File5():
    def __init__(self,filename):
        self.filename = filename
    def count_word(self):
        try:
            with open(self.filename) as f_os:
                cons = f_os.read()
        except FileNotFoundError:
            print('_________________')
        else:
            word = cons.splitlines()
            print("File len is :"+str(len(word)))

file = ['data.txt',"pi_digits.txt",'programming.txt',"ddd.txt","dadada.txt"]
for ls in file:
    f=File5(ls)
    f.count_word()

# # 把所有的程序都放在使用类---函数的形式进行修改。
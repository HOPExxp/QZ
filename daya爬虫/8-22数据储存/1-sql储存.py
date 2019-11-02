# import pymysql
#
# #PyMySQL的connect()方法声明一个MySQL连接对象db
# #传入mysql的host(IP),本地运行即localhost，用户名，密码，端口号.
# db = pymysql.connect(host='127.0.0.1',user='root', password='41632543xxp', port=3306)
# #调用cursor()方法获得MySQL的操作游标，利用游标来执行SQL语句
# cursor = db.cursor()
# #利用execute()方式获取版本号
# cursor.execute('SELECT VERSION()')
# #利用fetchone方法获取第一条数据
# data = cursor.fetchone()
# print('Database version:', data)
# #创建一个名为aa的数据库，默认编码为UTF8MB4,此数据库可以在mysql data目录下找到
# cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET UTF8MB4")
# db.close()


# import pymysql
#
# #PyMySQL的connect()方法声明一个MySQL连接对象db
# #传入mysql的host(IP),本地运行即localhost，用户名，密码，端口号.
# db = pymysql.connect(host='127.0.0.1',user='root', password='41632543xxp',
#                      db = 'spiders', port = 3306 )
# #调用cursor()方法获得MySQL的操作游标，利用游标来执行SQL语句
# cursor = db.cursor()
# create = '''CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL,
#  name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'''
# cursor.execute(create)
#
# db.close()

# import pymysql
#
# a = '2019002'
# name = 'xxp'
# age = 28
#
# db = pymysql.connect(host='127.0.0.1',user='root', password='41632543xxp',
#                      db = 'spiders', port = 3306 )
# cursor = db.cursor()
# # 构造一个sql语句，其value值通过格式化%s来实现
# # sql = 'INSERT INTO students(id, name, age) values(%s, %s, %s)'
# sql = 'INSERT INTO students(id, name, age) values("2019001","kuli",28)'
# # 通过execute()方法获取sql语句的学生元组信息
# try:
#     cursor.execute(sql)
#     db.commit()  # commit()方法实现数据插入
#     print(1)
# except:
#     db.rollback()  # 异常处理，如果执行失败则数据回滚。
#     print(0)
# db.close()

# import pymysql
#
# #定义变量名data里面传入的是学生信息
# data={
#    'id':'2019003',
#    'name':'xxp',
#    'age':25,
# }
# #把表名也做一个变量
# table = 'students'
# #通过join方法把data数据的字段名做个变量
# keys = ','.join(data.keys())
# print(keys)
# #通过join方法把data数据的values的值做个变量，其值通过占位符的形式传递，占位符的数量根据data数据的长度来变化
# values = ','.join(['%s']*len(data))
# print(values)
# #连接数据库spider
# db = pymysql.connect(host='127.0.0.1',user='root', password='41632543xxp',
#                      db = 'spiders', port = 3306 )
# #调用cursor()方法获得MySQL的操作游标，利用游标来执行SQL语句
# cursor = db.cursor()
# #利用格式化字符串format()方法将表名、字段名和值构造出来，
# sql = 'INSERT INTO {table}({keys}) VALUES({values})'.format(table=table, keys=keys, values=values)
# print(sql)
# #执行插入语句的表中写法
# try:
#     #导入value值--%s
#    if cursor.execute(sql,tuple(data.values())):
#       print(1)
#       db.commit()
# except:
#    print(0)
#    db.rollback()
# # cursor.execute(sql,tuple(data.values()))
# # pymysql.err.InternalError: (1054, "Unknown column 'gender' in 'field list'")
# db.close()


# 更新数据（主键存在时更新数据）
# import pymysql
#
# #定义变量名data里面传入的是学生信息
# data={
#    'id':'2019006',
#    'name':'xzf',
#    'age':18,
# }
# #把表名也做一个变量
# table = 'students'
# #通过join方法把data数据的字段名做个变量
# keys = ','.join(data.keys())
# #通过join方法把data数据的values的值做个变量，其值通过占位符的形式传递，占位符的数量根据data数据的长度来变化
# values = ','.join(['%s']*len(data))
# #连接数据库spider
# db = pymysql.connect(host='127.0.0.1',user='root', password='41632543xxp',
#                      db = 'spiders', port = 3306 )
# #调用cursor()方法获得MySQL的操作游标，利用游标来执行SQL语句
# cursor = db.cursor()
# #ON DUPLICATE KEY UPDATE意思是如果主键存在，就执行更新操作
# sql = 'INSERT INTO {table}({keys}) VALUES({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys, values=values)
# #定义update变量，用来判断主键是否存在，遍历data中的key
# update = ','.join([" {key} = %s".format(key=key) for key in data])
# print(update)
# sql += update#sql根据updata来变化
# print(sql)
# #执行插入语句的表中写法
# try:
#    #因为构造语句中sql的values占位符是6个s%，所以我们的元组也要乘2
#    if cursor.execute(sql,tuple(data.values())*2):
#       print(1)
#       db.commit()
# except:
#    print(0)
#    db.rollback()
# db.close()

# 更新数据-简易
# import pymysql
# db = pymysql.connect(host='127.0.0.1',user='root', password='41632543xxp',
#                      db = 'spiders', port = 3306 )
# #调用cursor()方法获得MySQL的操作游标，利用游标来执行SQL语句
# cursor = db.cursor()
# sql1 = 'update students set age = 20 where name = "xxp"'
# # sql1 = 'UPDATE students SET age = %s WHERE name = %s'#通过占位符的方式传参，修改数据
# try:
#     cursor.execute(sql1)
#     # cursor.execute(sql1,(18,'xxp'))
#     print(1)
#     db.commit()
# except:
#    print(0)
#    db.rollback()
# db.close()

# import pymysql
# db = pymysql.connect(host='127.0.0.1',user='root', password='41632543xxp',
#                      db = 'spiders', port = 3306 )
# #调用cursor()方法获得MySQL的操作游标，利用游标来执行SQL语句
# cursor = db.cursor()
# sql = 'select * from students'
# try:
#     cursor.execute(sql)
#     results = cursor.fetchall()
#     for res in results:
#         print(res)
# except:
#     print('error')

# ('2019001', 'kuli', 28)
# ('2019002', 'James', 25)
# ('2019003', 'xxp', 25)
# ('2019004', 'xxxp', 35)
# ('2019005', 'xxxxp', 35)


import pymysql
db = pymysql.connect(host='127.0.0.1',user='root', password='41632543xxp',
                     db = 'spiders', port = 3306 )
#调用cursor()方法获得MySQL的操作游标，利用游标来执行SQL语句
cursor = db.cursor()
sql = 'select * from students where age>=20'
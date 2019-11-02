#连接数据库的库
import MySQLdb
#连接地址、用户名--root、密码--、数据库--yiibaidb、charset--utf8
#连接数据库
db = MySQLdb.connect("localhost","root","41632543xxp","yiibaidb",charset = "utf8")
#使用cursor方法获取操作游标
cursor = db.cursor()
#使用xexcute方法执行sql语句

#****************************
#创建表
#如果表存在需要先删除
cursor.execute('DROP TABLE IF EXISTS EMPLOYEE')

#创建表
create_table = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,
         SEX CHAR(1),
         INCOME FLOAT )"""

#执行创建操作
cursor.execute(create_table)
#
# cursor.execute('DESC EMPLOYEE;')
#
# #使用fetchone方法获取一条数据
# data = cursor.fetchone()
# print(data)
#******************************************

#******************************************
# #插入数据
# insert_data = """INSERT INTO EMPLOYEE(FIRST_NAME,
#          LAST_NAME, AGE, SEX, INCOME)
#          VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
# try:
#    # 执行sql语句,只是写到内存中
#    cursor.execute(insert_data)
#    # 提交到数据库执行，写在硬盘中去
#    db.commit()
# except:
#      # 如果发生错误，还原到原来的状态
#      #数据不完整等异常
#      db.rollback()
#
# cursor.execute('SELECT * FROM EMPLOYEE')
#
# #使用fetchone方法获取一条数据
# data = cursor.fetchone()
# print(data)
#**********************************************

#**********************************************
# cursor.execute('SELECT * FROM EMPLOYEES')
# result = cursor.fetchall()
# print(result)
# 查询数据
# find_data = "SELECT * FROM EMPLOYEES \
#        WHERE OFFICECODE = 1"
# try:
#    # 执行SQL语句
#    cursor.execute(find_data)
#    # 获取所有记录列表
#    results = cursor.fetchall()
#    for row in results:
#       employeeNum = row[0]
#       lastName = row[1]
#       firstName = row[2]
#       email = row[4]
#       officecode = row[5]
#       # 打印结果
#       print("employeeNum=%-10s,lastName=%-10s,firstName=%-10s,email=%-25s,officecode=%-5s" % \
#              (employeeNum, lastName, firstName, email, officecode ))
# except:
#    print("Error: unable to fecth data")

############################################  mine

#查询数据
# find_data = "SELECT * FROM EMPLOYEE \
#        WHERE AGE > 19"
# try:
#    # 执行SQL语句
#    cursor.execute(find_data)
#    # 获取所有记录列表
#    results = cursor.fetchall()
#    for row in results:
#       fname = row[0]
#       lname = row[1]
#       age = row[2]
#       sex = row[3]
#       income = row[4]
#       # 打印结果
#       print("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
#              (fname, lname, age, sex, income ))
# except:
#    print("Error: unable to fecth data")
#******************************************

#******************************************
#更新数据
# sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = 'M'"
# try:
#    # 执行SQL语句
#    cursor.execute(sql)
#    # 提交到数据库执行
#    db.commit()
# except:
#    # 发生错误时回滚
#    db.rollback()
#
# cursor.execute('SELECT * FROM EMPLOYEE;')
#
# #使用fetchone方法获取一条数据
# data = cursor.fetchall()
# print(data)
#****************************************

#****************************************
#删除操作
# sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % (20)
# try:
#    # 执行SQL语句
#    cursor.execute(sql)
#    # 提交修改
#    db.commit()
# except:
#    # 发生错误时回滚
#    db.rollback()
#
# cursor.execute('SELECT * FROM EMPLOYEE;')

#使用fetchone方法获取一条数据
data = cursor.fetchone()
print(data)

#关闭数据库
db.close()
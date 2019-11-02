#连接数据库的库
import MySQLdb
#连接地址、用户名--root、密码--、数据库--yiibaidb、charset--utf8
#连接数据库
db = MySQLdb.connect(host = "localhost",user = "root",passwd = "41632543xxp",db = "yiibaidb",charset = "utf8",port = 3306)
#使用cursor方法获取操作游标
cursor = db.cursor()
#使用xexcute方法执行sql语句
cursor.execute('SELECT VERSION()')
#使用fetchone方法获取一条数据
data = cursor.fetchone()
print('database version:%s'%data)
#关闭数据库
db.close()
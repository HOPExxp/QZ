from redis import StrictRedis,ConnectionPool

# 方法一 -- strictredis（）
redis = StrictRedis(host='localhost',port=6379,db=0)
redis.set('name8','刘德华')
print(redis.get('name8').decode('utf-8'))

#方法二 -- connectionpool()
# pool = ConnectionPool(host='localhost',port=6379,db=0)
# redis = StrictRedis(connection_pool=pool)
# redis.set('name2','郭富城')
# print(redis.get('name2').decode('utf-8'))

#方法三 -- 通过connectionpool添加url的方式连接，支持远程连接
# 格式：redis://[:password]@host:port/db 如果没有密码可以不写
# url = 'redis://@localhost:6379/0'
# pool = ConnectionPool.from_url(url)
# redis = StrictRedis(connection_pool=pool)
# redis.set('name3','张学友')
# print(redis.get('name3').decode('utf-8'))

#键操作
# url = 'redis://@localhost:6379/0'
# pool = ConnectionPool.from_url(url)
# redis = StrictRedis(connection_pool=pool)
# print(redis.exists('name1'))
# # print(redis.delete('name1'))
# print(redis.type('name2'))
# print(redis.keys('n*'))
# # print(redis.move('name2',1))
# print(redis.flushdb())
# print(redis.flushall())

#字符串操作
# url = 'redis://@localhost:6379/0'
# pool = ConnectionPool.from_url(url)
# redis = StrictRedis(connection_pool=pool)
#set 、get
# redis.set('name0','Bob')
# print(redis.get('name0'))

#mset
# redis.mset({'name3':'xx','name4':'xxx'})

#mget
# a = redis.mget(['name0','name2','name3','name4'])
# print(a)

#getset
#取键原来的值，并赋一个新值 -- Mike
# a = redis.getset('name0','Mike')
# print(a)


#setex  将键值设置为新值，有效期为1s
# redis.setex('name0',15,'james')


# redis.set('name2','Hello')
# # setrange() -- 在index为6的位置补充Wrold
# redis.setrange('name2',6,'Wrold')
# # Hello\x00Wrold  redis数据库中
# print(redis.get('name2').decode('utf-8'))
# # Hello Wrold  python中

#getrange -- 截取‘name’对应值的指定部分
# a = redis.getrange('name2',1,8)
# print(a)

#setnx -- 如果键值对不存在，即设置，存在即不设置
# redis.setnx('name1','xxxxp')

#msetnx -- 多个键值对都不存在的情况下设置
# redis.msetnx({'name5':'aa','name6':'aaa'})

# incr -- age对应的值增加amount，若age键不存在，创建该值
# redis.set('name7',10)
# redis.incr('name7',2)
# print(redis.get('name7'))

# decr -- 对应的值减amount

#substr -- 截取键对应的字符串  同getrange ？？‘


#-------列表操作
# redis.rpush('list',1,2,3,4)  #列表尾添加
redis.lpush('list',0,-1,-2)  #列表头添加

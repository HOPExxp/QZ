import pymongo
from bson.objectid import ObjectId

#连接mongodb
client = pymongo.MongoClient(host='localhost',port=27017)

#创建数据库 -- test
db = client.test

#创建集合（表） -- collection
collection = db.students


# #插入一条数据
# student = {
#     'id':'2019001',
#     'name':'jordan',
#     'age':20,
#     'gender':'male'
# }
#
# result = collection.insert_one(student)
# print(result)

# #插入多条数据
# student1 = {
#     'id':'2019002',
#     'name':'alex',
#     'age':30,
#     'gender':'male'
# }
# student2 = {
#     'id':'2019003',
#     'name':'yuan',
#     'age':32,
#     'gender':'male'
# }
#
# result1 = collection.insert_many([student1,student2])
# print(result1)

#查询数据
#find_one方法
# result1 = collection.find_one({'id':'2019001'})
# result2 = collection.find_one({'id':'2019002'})
# result3 = collection.find_one({'id':'2019003'})
# # result4= collection.find_one()
# print(result1,result2,result3)
# {'_id': ObjectId('5d6518daef8d0ee32d8402f7'), 'id': '2019001', 'name': 'jordan', 'age': 20, 'gender': 'male'}
# {'_id': ObjectId('5d6529d4a6821950034a1b59'), 'id': '2019002', 'name': 'alex', 'age': 30, 'gender': 'male'}
# {'_id': ObjectId('5d6529d4a6821950034a1b5a'), 'id': '2019003', 'name': 'yuan', 'age': 32, 'gender': 'male'}

#结合objectId类查询
# result = collection.find_one({'_id':ObjectId('5d6529d4a6821950034a1b59')})
# print(result)

#find方法
#可以加条件查找  $in中所指的范围不是指一个区间
# result = collection.find({'age':{'$in':[20,35]}})   #全部找出，需要遍历取值
#
# print(result)
# # <pymongo.cursor.Cursor object at 0x000002AD1D922908>
# print(type(result))
# # <class 'pymongo.cursor.Cursor'>
# for i in result:
#     print(i)

#更新操作
# update（）方法   不推荐，已被抛弃
# DeprecationWarning: update is deprecated. Use replace_one, update_one or update_many instead.
# result = collection.update(res,student)
# res = {'name':'yuan'}
# student = collection.find_one(res)
# student['age'] = 50
# result = collection.update(res,student)
# print(result)

# update_one()方法
# res = {'name':'yuan'}
# student = collection.find_one(res)
# student['age'] = 60
# result = collection.update_one(res,{'$set':student})#$set操作符，改变原有值
# print(type(result))
# print(result.matched_count,result.modified_count)
# <class 'pymongo.results.UpdateResult'>
# 1 1

#update_one()方法的条件操作
#修改年纪大于20
# condition = {'age':{'$gt':25}}
# result = collection.update_one(condition,{'$inc':{'age':1}})#在原有值得基础上加1，返回的是满足条件的第一个值
# print(result)
# print(result.matched_count,result.modified_count)
# {'_id': ObjectId('5d6518daef8d0ee32d8402f7'), 'id': '2019001', 'name': 'jordan', 'age': 20, 'gender': 'male'}
# {'_id': ObjectId('5d6529d4a6821950034a1b59'), 'id': '2019002', 'name': 'alex', 'age': 31, 'gender': 'male'}
# {'_id': ObjectId('5d6529d4a6821950034a1b5a'), 'id': '2019003', 'name': 'yuan', 'age': 50, 'gender': 'male'}

#update_many()方法  -- 一次更新多个值
#修改年纪大于20
# condition = {'age':{'$gt':20}}
# result = collection.update_many(condition,{'$inc':{'age':1}})#在原有值得基础上加1，返回的是满足条件的第一个值
# print(result)
# print(result.matched_count,result.modified_count)
# {'_id': ObjectId('5d6518daef8d0ee32d8402f7'), 'id': '2019001', 'name': 'jordan', 'age': 20, 'gender': 'male'}
# {'_id': ObjectId('5d6529d4a6821950034a1b59'), 'id': '2019002', 'name': 'alex', 'age': 32, 'gender': 'male'}
# {'_id': ObjectId('5d6529d4a6821950034a1b5a'), 'id': '2019003', 'name': 'yuan', 'age': 51, 'gender': 'male'}


# res = collection.find()
# for i in res:
#     print(i)
# {'_id': ObjectId('5d6518daef8d0ee32d8402f7'), 'id': '2019001', 'name': 'jordan', 'age': 20, 'gender': 'male'}
# {'_id': ObjectId('5d6529d4a6821950034a1b59'), 'id': '2019002', 'name': 'alex', 'age': 30, 'gender': 'male'}
# {'_id': ObjectId('5d6529d4a6821950034a1b5a'), 'id': '2019003', 'name': 'yuan', 'age': 62, 'gender': 'male'}

#删除操作
# delete_one()方法
#result = collection.delete_one({'age':{'$gt':30}})
#print(result)
# result = collection.delete_many({'age':{'$gt':30}})
# print(result)
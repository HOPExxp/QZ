#datetime库 .date  .time  .datetime  .timedelta(时间分隔)   .tzinfo(时区)
#主讲 datetime对象
from datetime import datetime


# #当前的日期和时间
# print(datetime.now())
# #当前日期和时间的utc（世界标准时间）表示
# print(datetime.utcnow())
# #自定义设置
# print(datetime(2019,9,16,22,34,32,7))

#datetime对象的属性  year month day hour minute second microsecond  min-最小时间对象  max-最大时间对象

#datetime对象的3种常用时间格式化方法

someday = datetime(2019,8,15,22,33,44,5555)
print(someday,type(someday))
#isoformat   返回ISO 8601标准显示时间
print(someday.isoformat())
#isoweekday  返回星期数  1-7
print(someday.isoweekday())
#shiftime   根据格式化字符串输出指定的字符串时间
print(someday.strftime('%Y-%m-%d %X'))
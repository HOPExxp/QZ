#类是对象的抽象    对象是类的实现,对象共有的特性放在类里面实现
# 类的基本使用  ,类可以多次的实例化，每次实例化都产生一个新的对象

class Car():
  def __init__(self,make,model,mk_year):
    self.make = make
    self.model = model
    self.mk_year = mk_year
    self.old_miles = 0
  def discrib(self):
    full_name ="this car name:"+str(self.make) + "this model is :"+str(self.model)+ str(self.mk_year)
    return  full_name
  def read_miles(self):
    print("This car miles:"+str(self.old_miles))
  # 一次性的更新
  def update_miles(self,miles):
    if miles >= self.old_miles:
       self.old_miles = miles
    else:
      print("非法操作")
  # 动态的更新
  def zzh_miles(self,miles):
    if miles >= 0:
      self.old_miles += miles
    else:
      print("非法操作，输入负值，你在作弊")
  #加油汽车
  def fill_tank(self,tank):
    print('the oil is' + str(tank))
# 电动车
#  定义一个函数，10--50公里，公里的增加，容量减少
#  定义一个充电  电量不足20，电量就会增加到100

class ElecCar(Car):
  def __init__(self,make,model,year):
    super().__init__(make,model,year)
    self.bettery = 100
  def describ_battery(self):
    print("This  car  battery cap:"+str(self.bettery))

  #消耗油并减少电池容量
  def consume_battery(self,mile):
    if mile > 500:
      print('超出一次行驶所允许最大距离')
    else:
      self.bettery -= mile * 0.2
      print('开一段时间后电量：'+str(self.bettery))
    # #电量低于预定值自动充电
    # if self.bettery < 20:
    #   ElecCar.charge_baterry(self)
  #电池低于预定值充电
  def charge_baterry(self):
    if self.bettery < 20:
      self.bettery = 100
      print('充电后电量为：'+ str(self.bettery))
    else:
      print('当前电量高于预定值，不需要充电，请过段时间再来充电')
      print('现在的电量为：' + str(self.bettery))
  #重写父类的fill_tank方法，转接充电方法
  def fill_tank(self,tank):
    print('----------------')
    print('先生，不好意思，我是电动车，不吃油,只能充电')
    print('为您转接充电服务')
    print('----------------')
    ElecCar.charge_baterry(self)

my_car = ElecCar("三星 ","奥拓 "," 2019")
mile_ = int(input('请输入走的公里数：'))
print('初始电量：',end=' ')
my_car.describ_battery()
# print('开一段时间后电量：',end=' ')
my_car.consume_battery(mile_)
# my_car.describ_battery()
# print('充电后电量：',end=' ')
my_car.charge_baterry()
# my_car.describ_battery()
# print('加油后电量：',end=' ')
# my_car.fill_tank(30)
# my_car.describ_battery()
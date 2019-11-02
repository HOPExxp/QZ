# 定义一个生产函数：实现生产自行车（手动输入），要求自行车要有两个字段，(号码,名字).一次性只能生产二十个。

def create(num='0',name='死飞'):
    byc = {}
    byc_list = []
    for i in range(20):
        byc['num'] = input('输入号码：')
        if byc['num'] == '':
            byc['num'] = num
        byc['name'] = input('输入名字：')
        if byc['name'] == '':
            byc['name'] = name
        # byc_list.append(byc)
        byc1 = byc.copy()
        byc_list.append(byc1)
    return byc_list
#     print(byc_list)
# print(create())

# 更改上一个生产函数为一个批量生产的函数。一次性生产30两自行车。把前10两批量车变成宝马（号码，名字）
def change_create():
    # start_byc = create(num,name)
    byc = {}
    byc_list1 = []
    byc_list2 = []
    #批量生产30个外星人
    for i in range(30):
        byc['num'] = i + 1
        byc['name'] = '死飞'
        byc1 = byc.copy()
        byc2 = byc.copy()
        byc_list1.append(byc1)
        byc_list2.append(byc2)
    #记录修改的自行车的信息
    byc_list2 = byc_list2[:10]
    #对前十辆自行车修改
    for j in byc_list1[:10]:
        j['num'] += 30
        j['name'] = '宝马'
        # byc2 = j.copy()
        # byc_list2.append(byc2)
        # j.clear()
    print('修改的自行车为：'+str(byc_list2))
    return byc_list1

print(change_create())

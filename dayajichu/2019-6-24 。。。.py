# 写一个产生球员的函数，要求不管来多少个球员，就只有5个位置（后卫，得分后卫，小前锋，大前锋，中锋），采用循环的方式产生。比如来了10个球员，1、6-后卫  2、7-得分后卫  3、8—小前锋  4、9—大前锋  5、10----后卫(中锋)。
# 并且要单独有一个字段，表示球队的，也就是说输入给这个函数的时候，球队只有一个，球员可以任意个。

def create_player(number,teamname):
    后卫_list = []
    得分后卫_list = []
    小前锋_list = []
    大前锋_list = []
    中锋_list = []
    for i in range(int(number)):
        if (i + 1 ) % 5 == 1:
            后卫_list.append(i + 1)
        elif (i + 1 ) % 5 == 2:
            得分后卫_list.append(i + 1)
        elif (i + 1) % 5 == 3:
            小前锋_list.append(i + 1)
        elif (i + 1) % 5 == 4:
            大前锋_list.append(i + 1)
        elif (i + 1) % 5 == 0:
            中锋_list.append(i + 1)
        else:
            pass
    # list1 = list[后卫_list,得分后卫_list,小前锋_list,大前锋_list,中锋_list]
    # return list1
    return 后卫_list,得分后卫_list,小前锋_list,大前锋_list,中锋_list,teamname

teamname = input('请输入球队名称：')
number = input('请输入全队总人数：')
# print(create_player(number,teamname))
print('球队名称为：' + str(create_player(number,teamname)[5]))
print('后卫:' + str(create_player(number,teamname)[0]))
print('得分后卫:' + str(create_player(number,teamname)[1]))
print('小前锋:' + str(create_player(number,teamname)[2]))
print('大前锋:' + str(create_player(number,teamname)[3]))
print('前锋:' + str(create_player(number,teamname)[4]))


# #方式2
#
# teamname = input('请输入球队名称：')
# number = input('请输入全队总人数：')
# qiuyuan = []
# for i in range(int(number)):
#     qiuyuan.append( i + 1 )
# # print(qiuyuan)
# def create_player(qiuyuan,teamname):
#     后卫_list = []
#     得分后卫_list = []
#     小前锋_list = []
#     大前锋_list = []
#     中锋_list = []
#     # print(qiuyuan)
#     for a in qiuyuan[::5]:
#         # print(a)
#         后卫_list.append(a)
#     for b in qiuyuan[1::5]:
#         得分后卫_list.append(b)
#     for c in qiuyuan[2::5]:
#         小前锋_list.append(c)
#     for d in qiuyuan[3::5]:
#         大前锋_list.append(d)
#     for e in qiuyuan[4::5]:
#         中锋_list.append(e)
#     return 后卫_list,得分后卫_list,小前锋_list,大前锋_list,中锋_list,teamname
#
# # print(create_player(number,teamname))
# print('球队名称为：' + str(create_player(qiuyuan,teamname)[5]))
# print('后卫:' + str(create_player(qiuyuan,teamname)[0]))
# print('得分后卫:' + str(create_player(qiuyuan,teamname)[1]))
# print('小前锋:' + str(create_player(qiuyuan,teamname)[2]))
# print('大前锋:' + str(create_player(qiuyuan,teamname)[3]))
# print('前锋:' + str(create_player(qiuyuan,teamname)[4]))

# 定义两个函数：
# 一个函数产生30个小怪物的字典列表，怪物的属性包括，color, name, high, weiht.
# 另一个函数调用第一个函数，并且手动输入杀死的怪物的数量，在字典列表中减少相应的怪物数量，
# 并且输出剩余的怪物数量。比如开始有30个，现在手动输入了3，那么就把怪物的个数变成27个，输出剩余27个怪物。
# 要求输入的杀死的怪物的数量不能大于剩余的怪物总数量

def create_monsters():
    monsters = []
    for i in range(30):
        monster = { 'color':'yellow','name':'daya','high':'200','weight':'200'}
        monsters.append(monster)
    return monsters

def kill_monsters():
    try:
        start_monsters = create_monsters()
        print('请输入你想要杀死的怪物数量：',end='')
        num = input()
        # if int(num)<=30:
        #     pass
        for j in range(int(num)):
            start_monsters.pop()
        print('剩余怪物的数量为：' + str(len(start_monsters)))
    except:
        print('你输入的数量超出范围！')

kill_monsters()

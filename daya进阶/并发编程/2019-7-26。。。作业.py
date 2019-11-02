#实现一个吃饭的过程：做饭，洗菜，做菜，吃饭，洗碗的过程，注意做成一个线程序列，顺序执行

import time,random,queue
from threading import Thread

q = queue.Queue()

#做饭
def male_meal(maker,i):
    print('{} is steaming rice {}'.format(maker,i))
    time.sleep(3)
    # print('meal is done')
    q.put('rice')
    print('maker {} has made rice{}'.format(maker,i))
    print('ok.....')
#洗菜
def xicai(maker):
    print('{} is washing vegetables'.format(maker))
    time.sleep(3)
    # q.put('vegetables')
    print('maker {} has washed vegetables'.format(maker))
    print('ok.....')
#做菜
def zuocai(maker,j):
    # count = 1
    # while count<5:
    print('{} is making maels'.format(maker))
    time.sleep(3)
    q.put('meal {}'.format(j))
    print('mael {} is done'.format(j))
    print('ok.....')
        # count+=1
#吃饭
def eat_meals(eater):
    print('now {} can eat meal'.format(eater))
    time.sleep(3)
    meal = q.get()
    print('eater {} has eaten {}'.format(eater,meal))
    print('ok.....')
#洗碗
def wash_dishes(washer):
    print('{} begin to wash dishes'.format(washer))
    time.sleep(3)
    if not q.empty():
        remain = q.get()
        print('{} has washed {}'.format(washer,remain))
    else:
        print('all dishes is washed')
        print('ok.....')
#主函数
if __name__ == '__main__':
    #做好四份饭
    for i in range(1,4):
        make = Thread(target=male_meal,args=('mother',i,))
        time.sleep(1)
        make.start()
    #吃饭
    eat1 = Thread(target=eat_meals,args=('son',))
    eat2 = Thread(target=eat_meals,args=('daughter',))
    eat3 = Thread(target=eat_meals,args=('father',))

    eat1.start()
    eat2.start()
    eat3.start()
    #洗菜
    xicai_0 = Thread(target=xicai, args=('mother',))
    xicai_0.start()
    #做4样菜
    for j in range(1,5):
        make_0 = Thread(target=zuocai,args=('mother',j))
        time.sleep(1)
        make_0.start()
    #吃菜
    eat1 = Thread(target=eat_meals,args=('son',))
    eat2 = Thread(target=eat_meals,args=('daughter',))
    eat3 = Thread(target=eat_meals,args=('father',))

    eat1.start()
    eat2.start()
    eat3.start()
    #洗碗
    wash = Thread(target=wash_dishes, args=('father',))

    wash.start()

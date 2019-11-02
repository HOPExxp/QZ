# 1、在一个主线程内设置两个线程，一个受时间控制，在一段时间后才开启，另一个受event控制，设置event后才开启

import threading
import time
import logging

# logging.basicConfig(
#     level=logging.DEBUG,
#     format='[%(threadName)-15s] %(message)s',
# )

#定时器线程
def time_control():
    print('['+threading.current_thread().getName()+']','('+'time\'s up,running'+')',time.ctime())

#event同步条件
def event_control(event):
    print('['+threading.current_thread().getName()+']','('+'wait for event set'+')',time.ctime())
    event.wait()
    print('['+threading.current_thread().getName()+']','('+'running event_control'+')',time.ctime())

if __name__ == '__main__':

    #class threading.Timer(interval, function, args=[], kwargs={})
    #创建一个timer，在interval秒过去之后，它将以参数args和关键字参数kwargs运行function 。
    #interval秒内不影响其他任务的执行
    time_threading = threading.Timer(interval = 8, function = time_control)
    time_threading.setName('time_control')

    #event控制
    event = threading.Event()
    event_threading = threading.Thread(target=event_control,args=(event,))
    event_threading.setName('event_control')

    #开启定时器线程
    print('['+threading.current_thread().getName()+']','('+'start timer'+')',time.ctime())
    time_threading.start()
    # logging.debug('end timer',time.ctime())

    #线程同步条件event
    print('['+threading.current_thread().getName()+']','('+'waiting before setting Event'+')',time.ctime())
    event_threading.start()
    time.sleep(2)
    event.set()
    print('['+threading.current_thread().getName()+']','('+'Evnet is set'+')',time.ctime())

    #主线程
    print('['+threading.current_thread().getName()+']','('+'end......'+')',time.ctime())
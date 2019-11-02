
# # coding: utf-8
# from threading import Timer
# import time
#
# def fun():
#     print ("hello, world")
#
# if __name__=='__main__':
#     t = Timer(5.0, fun)
#     print(time.ctime())
#     t.start() # 5秒后, "hello, world"将被打印
#     print(time.ctime())


#
# # 1、在一个主线程内设置两个线程，一个受时间控制，在一段时间后才开启，另一个受event控制，设置event后才开启
#
# import threading
# import time
# import logging
#
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='[%(threadName)-15s] %(message)s',
# )
#
# def time_control():
#     logging.debug('time\'s up,running')
#
# def event_control(event):
#     logging.debug('wait for event set')
#     event.wait()
#
# if __name__ == '__main__':
#     time_threading = threading.Timer(interval = 1, function = time_control)
#     time_threading.setName('time_control')
#
#     event = threading.Event()
#     event_threading = threading.Thread(target=event_control,args=(event,))
#     event_threading.setName('event_control')
#
#     #开启定时器线程
#     logging.debug('start timer')
#     time_threading.start()
#     # logging.debug('end timer')
#
#     #线程同步条件event
#     logging.debug('waiting before setting Event')
#     time.sleep(2)
#     event.set()
#     logging.debug('Evnet is set')
#
#     #主线程
#     logging.debug('end......')


print('\033[32;1mConsumer %s has eat baozi...' %('Hello'))
# print('\033[0;32;47' ,('Hello'))
# print('*' * 50)
print('\033[32mhello')
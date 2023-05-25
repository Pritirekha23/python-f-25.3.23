from threading import *
import time

#ex-1
#check main thread is a daemon thread or not
# print('Main thread is daemon:',current_thread().daemon)
#o/p--> False

#ex-2

# def fun1():
#     for i in range(5):
#         print(i)
#         time.sleep(1)

# t1=Thread(target=fun1)
# print('t1 is daemon:',t1.daemon)
# t1.start()

'''t1 is daemon: False
0
1
2
3
4'''

#ex-3 (set t1 thread as a daemon thread)

# def fun1():
#     for i in range(5):
#         print(i)
#         time.sleep(1)

# t1=Thread(target=fun1,daemon=True)
# print('t1 is daemon:',t1.daemon)
# t1.start()
# print('End of the main thread')
#o/p
# t1 is daemon: True
# 0
# End of the main thread


#ex-4
# def fun1():
#     for i in range(5):
#         print(i)
#         time.sleep(1)

# t1=Thread(target=fun1,daemon=True)
# print('t1 is daemon:',t1.daemon)
# t1.start()
# time.sleep(3)
# print('End of the main thread')

# o/p
# t1 is daemon: True
# 0
# 1
# 2
# End of the main thread

#ex-5
''' here t1 is not daemon so it will execute fully
def fun1():
    for i in range(5):
        print(i)
        time.sleep(1)

t1=Thread(target=fun1)
print('t1 is daemon:',t1.daemon)
t1.start()
time.sleep(3)
print('End of the main thread')

o/p:
t1 is daemon: False
0
1
2
End of the main thread
3
4
'''


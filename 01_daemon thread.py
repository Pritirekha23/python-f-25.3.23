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
#ex-6
'''
def fun():
    for i in range(5):
        print('Hi')
        time.sleep(1)
    t2=Thread(target=fun1)
    t2.start()
def fun1():
    for i in range(5):
        print('Hello')
        time.sleep(1)

t1=Thread(target=fun,daemon=True)
print('t1 is daemon:',t1.daemon)
t1.start()
time.sleep(10)
print('End of the main thread')

o/p
t1 is daemon: True
Hi
Hi
Hi
Hi
Hi
Hello
Hello
Hello
Hello
Hello
End of the main thread '''
#ex-7
'''
def fun():
    for i in range(5):
        print('Hi')
        time.sleep(1)
    t2=Thread(target=fun1)
    print('t2 is daemon:',t2.daemon)
    t2.start()
def fun1():
    for i in range(5):
        print('Hello')
        time.sleep(1)

t1=Thread(target=fun,daemon=True)
print('t1 is daemon:',t1.daemon)
t1.start()
time.sleep(10)
print('End of the main thread')

t1 is daemon: True
Hi
Hi
Hi
Hi
Hi
t2 is daemon: True
Hello
Hello
Hello
Hello
Hello
End of the main thread '''

#ex-8
'''
def fun():
    for i in range(5):
        print('Hi')
        time.sleep(1)
    t2=Thread(target=fun1)
    print('t2 is daemon:',t2.daemon)
    t2.start()
def fun1():
    for i in range(5):
        print('Hello')
        time.sleep(1)

t1=Thread(target=fun,daemon=True)
print('t1 is daemon:',t1.daemon)
t1.start()
time.sleep(5)
print('End of the main thread')

t1 is daemon: True
Hi
Hi
Hi
Hi
Hi
End of the main thread '''

#ex-9
'''def fun():
    for i in range(5):
        print('Hi')
        time.sleep(1)
    t2=Thread(target=fun1,daemon=False)
    print('t2 is daemon:',t2.daemon)
    t2.start()
def fun1():
    for i in range(5):
        print('Hello')
        time.sleep(1)

t1=Thread(target=fun,daemon=True)
print('t1 is daemon:',t1.daemon)
t1.start()
time.sleep(7)
print('End of the main thread')

t1 is daemon: True
Hi
Hi
Hi
Hi
Hi
t2 is daemon: False
Hello
Hello
End of the main thread
Hello
Hello
Hello'''

#ex-10
'''
def sec_count():
    sec=0
    while True:
        time.sleep(4)
        sec=sec+4
        print(f'I am waiting since {sec} second')

t1=Thread(target=sec_count,daemon=True)
t1.start()
name=input('Enter your name:\n')

Enter your name:
I am waiting since 4 second
I am waiting since 8 second
I am waiting since 12 second
I am waiting since 16 second
priti
'''

#ex-11
# traditinal approach
#isDaemon()->used to check a thread is daemon or not.
'''print('main thread i daemon :',current_thread().isDaemon())

output:
DeprecationWarning: isDaemon() is deprecated, get the daemon attribute instead        
  print('main thread i daemon :',current_thread().isDaemon())
main thread i daemon : False '''

#setDaemon
'''def fun1():
    for i in range(3):
        print('jin')
        time.sleep(2)
t1=Thread(target=fun1)
t1.setDaemon(True)
t1.start()

output:
_daemon thread.py:249: DeprecationWarning: setDaemon() is deprecated, set 
the daemon attribute instead       
  t1.setDaemon(True)
jin'''

#NOTE:
'''Once a thread started then we cant change its nature '''

'''def fun1():
    for i in range(2):
        print('jimin')
        time.sleep(2)
t1=Thread(target=fun1)
t1.start()
t1.daemon=True 
#t1 thread already started but here we are trying to set t1 as daemon so it cant be daemon.

output:
daemon status of active thread")   
RuntimeError: cannot set daemon status of active thread
jimin
'''

#main thread is non daemon by default can we change its nature (ans: no we cant change)

current_thread().daemon=True

# output:
#  RuntimeError("cannot set 
# daemon status of active thread")   
# RuntimeError: cannot set daemon status of active thread
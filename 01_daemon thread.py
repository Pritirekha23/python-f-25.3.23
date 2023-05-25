from threading import *
import time

#ex-1
#check main thread is a daemon thread or not
print('Main thread is daemon:',current_thread().daemon)
#o/p--> False
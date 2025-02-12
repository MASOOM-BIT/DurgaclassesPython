#to check a thread is dead or live
#function : isAlive() it will return True or False
from threading import *
import time
def display():
    print(current_thread().name)

t1=Thread(target=display,name='child_thread-1')
t2=Thread(target=display,name='child_thread-2')
t3=Thread(target=display,name='child_thread-3')
t4=Thread(target=display,name='child_thread-4')
t1.start()
print(t1.name)
print('isAlive',t1.is_alive())
t2.start()
t3.start()
t4.start()
thread_list=enumerate()
for t in thread_list:
    print('Name:',t.name)
    print('Id no:',t.ident)

print(t2.name)
print('isAlive',t2.is_alive())
time.sleep(10)
print(t1.name)
print('isAlive',t1.is_alive())
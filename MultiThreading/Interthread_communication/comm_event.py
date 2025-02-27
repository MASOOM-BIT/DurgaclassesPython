#if t1 update is not ready, t2 has to wait. As soon as t1 update is complete, it will signal t2 to get this update and perform

#Event: Event is the simplest communication mechanism between the thread , one thread signal an event and other thread wait for it.

#Creating an event 
#e=Event()
#e.set()
#e.clear()
#e.isSet()
#e.wait()

from threading import *
import time
e=Event()
def consumer():
    print('Consumer thread is waiting for updation')
    e.wait()
    print('Consumer got notification and consuming items')

def producer():
    time.sleep(5)
    print('Producer thread producing items')
    print('Producer thread giving notification by setting the event')
    e.set()

t1=Thread(target=consumer)
t2=Thread(target=producer)
t1.start()
t2.start()

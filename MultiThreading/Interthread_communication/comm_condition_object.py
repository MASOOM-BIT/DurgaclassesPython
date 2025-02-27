#c=Condition()
#c.acquire()
#c.wait()
#c.wait(time)
#c.notify()
#c.notifyAll()
#c.release()

from threading import *
import time
def consumer(c):
    c.acquire()
    print('Consumer waiting for updation')
    c.wait()
    print('Consumer got notification and consuming items')
    c.release()

def producer(c):
    c.acquire()
    print('Producer thread producing items')
    print('Producer thread giving notification by setting the condition')
    time.sleep(5)
    c.notify()
    c.release()

c=Condition()
t1=Thread(target=consumer,args=(c,))
t2=Thread(target=producer,args=(c,))
t1.start()
t2.start()

    


#s=Semaphore(no of threads)
#it is used to limit the number of threads that can access the resource

from threading import *
import time
s=Semaphore(2)

def wish(name):
    s.acquire()
    for i in range(10):
        print("Good Morning :",end='')
        time.sleep(2)
        print(name)
    s.release()

t1=Thread(target=wish,args=('Durga',))
t2=Thread(target=wish,args=('Ravi',))
t3=Thread(target=wish,args=('Shiva',))
t4=Thread(target=wish,args=('Mahesh',))
t1.start()
t2.start()
t3.start()
t4.start()
from threading import *
import time
l=Lock()

def Wish(name):
    l.acquire()
    for i in range(10):
        print("Good Morning :",end='')
        time.sleep(1)
        print(name)
    l.release()

t1=Thread(target=Wish,args=('Durga',))
t2=Thread(target=Wish,args=('Ravi',))
t1.start()
t2.start()




from threading import *
import time

import random
items=[]
def produce(c):
    while True:
        c.acquire()
        item=random.randint(1,100)
        print(f"Producer is producing {item}")
        items.append(item)
        print('producer is producing item')
        c.notify()
        c.release()
        time.sleep(5)

def consume(c):
    while True:
        c.acquire()
        print('consumer is waiting for item')
        c.wait()
        print('consumer is consuming item')
        item=items.pop()
        print(f"Consumer is consuming {item}")
        c.release()

c=Condition()
t1=Thread(target=produce,args=(c,))
t2=Thread(target=consume,args=(c,))
t1.start()
t2.start()

        

# to solve re-entrant problem of lock we use RLock
from threading import *
import time
r=RLock()

def factorial(n):
    r.acquire()
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    r.release()
    return result
def result_display(n):
    print(f'The factorial of {n} is {factorial(n)}')

t1=Thread(target=result_display,args=(5,))
t2=Thread(target=result_display,args=(9,))
t1.start()
t2.start()

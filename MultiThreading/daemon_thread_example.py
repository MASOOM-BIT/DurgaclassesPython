from threading import *
import time
def job1():
    print('Job-1 Executed')
    print(current_thread().name,current_thread().daemon)
    t2=Thread(target=job2 , name='Child-thread-2')
    t2.start()

def job2():
    print('Job2 Execution')
    print(current_thread().name,current_thread().daemon)

t1=Thread(target=job1,name='Child Thead-1')
t1.setDaemon(True)
t1.start()
time.sleep(10)

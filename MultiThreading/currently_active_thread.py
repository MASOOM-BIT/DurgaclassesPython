#active_count()
from threading import *
import time
def display():
    print(current_thread().name,"started")
    time.sleep(5)
    print(current_thread().name,'Ended')
print('No of active thread',active_count())
t1=Thread(target=display,name='child_thread-1')
t2=Thread(target=display,name='child_thread-2')
t1.start()
t2.start()
print()
print('No of active thread',active_count())

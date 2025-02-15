#If a Thread wants to wait until some other thread to then we should go for join methods
# Syntax : thread_object.join()
#Waiting for a specific time
# Syntax : thread_object.join(10)

from threading import *
import time

def display():
    for i in range(10):
        print('Jane Thread')
        time.sleep(5)

t=Thread(target=display)
t.start()
t.join()
for i in range(10):
    print('Lisbon Thread')
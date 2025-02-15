#To understand simple working of multiple thread
from threading import *
def display():
    for i in range(10):
        print('Child thread or thread-01')
    
t=Thread(target=display)
t.start()
for i in range(10):
    print('Main Thread')

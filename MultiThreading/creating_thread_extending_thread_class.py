from threading import *
class My_thread(Thread):
    def run(self): #already available method in thread class
        for i in range(10):
            print('Executed by child thread -1')

t=My_thread() # No need to target as child job is already defined thread class
t.start()
for i in range(10):
    print('Main thread -1')


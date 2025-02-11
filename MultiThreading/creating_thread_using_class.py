from threading import *
class Test:
    def display(self):
        for i in range(10):
            print(current_thread().getName())

t=Test()
thread_init = Thread(target=t.display)
thread_init.start()
for i in range(10):
    print(current_thread().getName())
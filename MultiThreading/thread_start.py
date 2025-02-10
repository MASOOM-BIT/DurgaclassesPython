'''
> Python provides in-built module
> module : threading
> thread : independent part of program
> An independent flow of execution
>>> single threaded program : Only one thread one by one execution
>>> multi threaded program : Multiple flow of execution on each thread responsible for some task/job
> Threading module
    current_thread() -> current executing thread object
    current_thread().getName()
        by Default : main_thread
'''

import threading
print('current thread : ',threading.current_thread().getName())

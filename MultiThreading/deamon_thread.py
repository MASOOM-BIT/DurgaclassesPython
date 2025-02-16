'''
> n number of people work in background to complete a movie. We never see them in a movie scree.
> The People who are working on background and never comes to screen is called daemon person
> Thus, Threads which are running in the background , those background executing thread by default consider as daemon thread

> purpose of deamon thread : to provide support to main thread
ex . gc 

>>> to find out deamon thread :
syntax:
t.isDeamon() or t.daemon
> Main Thread is always non-daemon

'''
from threading import *
print(current_thread().isDaemon())
print(current_thread().daemon)

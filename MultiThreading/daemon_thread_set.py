#Main thread is always non-daemon
#for all remaining thread daemon nature will be inherited from parent

from threading import *
import time
def job():
    print('child Thread')

t1=Thread(target=job)
print(t1.daemon)
t1.setDaemon(True)
print(t1.daemon)

#purpose of deamon thread:
#To Provide support for non daemon thread
#Last non-daemon thread terminate there is no use of daemon thread

from threading import *
def job2():
    for i in range(10):
        print('Lazy thread')
        time.sleep(3)

t2=Thread(target=job2)
t2.start()
time.sleep(5)
print('End is Main thread') 

# output :
# Lazy thread
# Lazy thread
# End is Main thread
# Lazy thread
# Lazy thread
# Lazy thread
# Lazy thread
# Lazy thread
# Lazy thread
# Lazy thread
# Lazy thread  : Main thread is completed and still child thread is executing because inherently child thread is non-deamon
print('------------------------------------------------------------')
# >>> setting child thread as Daemon thread
def job3():
    for i in range(10):
        print('child thread')
        time.sleep(3)

t3=Thread(target=job3)
t3.setDaemon(True)
t3.start()
time.sleep(5)
print('End is Main thread')
# Lazy thread
# Lazy thread
# End is Main thread  >>>> child thread is terminate as soon as parent terminate
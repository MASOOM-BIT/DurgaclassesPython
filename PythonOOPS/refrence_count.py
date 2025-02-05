#To find no of Refrence related to a objects

import sys
class Test:
    pass

t1=Test
t2=t1
t3=t1
t4=t1

print('No of refrence to a Object: ',sys.getrefcount(t1))
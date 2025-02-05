'''
>>> Destructors:
> destructor is called by GC to perform destruction of object
syntax : __del__()
> 'gc' always call destructor to perform cleanup code before destroying object
> to fullfill last wish 'gc' will call 
__del__(self):
    #cleanup code

> the job of destructor is to perform cleanup cactivities just before destroying an object
> destroctor never destroy object 'gc' do
'''
# Example 1
import time
class Test:
    def __init__(self):
        print('Objects intilixation')
    def __del__(self):
        print("Fullfulling last wish/Clean Activity") #execte auto as soon as t1=Nonw will execute

t1=Test()
t1=None #Now eligible for gc
time.sleep(5)
print('End of Application')

# Example 2
class Test:
    def __init__(self):
        print('Constructor Executed')
    def __del__(self):
        print('Deconstructor Executed')

t1=Test()
del t1
time.sleep(5)
print('End')
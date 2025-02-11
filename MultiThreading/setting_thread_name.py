#To get/set own name to the thread
# syntax:
# t.getName() ->> get thread Name
# t.setName(name) ->> set thread Name
# t.name

from threading import *
print(current_thread().getName())

current_thread().setName('OriginalMasoomThread')
print(current_thread().getName())
print(current_thread().name)


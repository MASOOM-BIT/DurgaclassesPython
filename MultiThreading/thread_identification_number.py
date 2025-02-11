#for every thread a unique identification number are there internally
# ident -> Access by using implicit variable

from threading import *
def Test():
    print('Child thread - 01')

t=Thread(target=Test)
t.start()
print('Main thread id no:',current_thread().ident)
print('Child thread id no:',t.ident)
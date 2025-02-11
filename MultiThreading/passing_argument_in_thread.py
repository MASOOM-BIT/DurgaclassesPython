from threading import *

def doubles(numbers):
    for n in numbers:
        print('Double:',2*n)

def squares(numbers):
    for i in numbers:
        print('squares: ',i*i)

numbers = [1,2,3,4,5]

t1=Thread(target=doubles,args=(numbers,))
t2=Thread(target=squares,args=(numbers,))
t1.start()
t2.start()
t1.join()
t2.join()#main thread will wait till child thread will execute
print('Jobs completed')

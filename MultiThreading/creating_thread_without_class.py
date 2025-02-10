from threading import *
def display():
    print('This code executed by main thread') #child thread
    print(current_thread().getName()) #child thread
print(current_thread().getName()) #main thread
t=Thread(target=display) #main 
print(current_thread().getName()) #main


t.start() #main thread

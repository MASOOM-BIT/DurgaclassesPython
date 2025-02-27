from threading import *
import time
e=Event()

def traffic_police():
    while True:
        time.sleep(10)
        print('Traffic police giving green signal')
        e.set()
        time.sleep(20)
        print('Traffic police giving red signal')
        e.clear()

def driver():
    num=0
    while True:
        print('Driver waiting for green signal')
        e.wait()
        print('Traffic is green, driving...')
        while e.isSet():
            num=num+1
            print('Number of cars passed:',num)
            time.sleep(2)
        print('Traffic is red, waiting for green signal')

t1=Thread(target=traffic_police)
t2=Thread(target=driver)
t1.start()
t2.start()

        

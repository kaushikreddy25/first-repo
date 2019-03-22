'''
Created on 20-Mar-2019

@author: guruk
'''
from threading import *
from time import sleep


class hi(Thread):
    def run(self):
        for i in range(5):
            print('Hi ')
            sleep(0.5)


class hello(Thread):
    def run(self):
        for i in range(5):
            print('Hello ')
            sleep(0.5)


t1 = hi()
t2 = hello()

t1.start()
sleep(0.1)
t2.start()

t1.join()
t2.join()
print('bye')
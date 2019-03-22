'''
Created on 11-Mar-2019

@author: guruk
'''
def sq(a):
    return a*a

res = sq(5)
print(res)

print('---------------')

f= lambda b: b*b

print(f(5))
'''
use when function has only one expression.
'''
print('------------------------')

d = lambda k,l : k+l

print(d(4,3))

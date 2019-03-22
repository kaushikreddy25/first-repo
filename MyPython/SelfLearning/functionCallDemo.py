'''
Created on 06-Mar-2019

@author: guruk
'''
def update(y):
    print('y - before ',y)
    print(id(y))
    y=10
    print('y - after ',y)
    print('after ', id(y))

a = 13
update(a)
print('a ',a)
print(id(a))   

#integers are immutable objects

print('----------------------')

def updatel(lis):
    print('lis - before ',lis)
    print(id(lis))
    lis[1] = 10
    print('lis - after ',lis)
    print('after ', id(lis))

lise = [13, 15, 20]
updatel(lise)
print('original list ',lise)
print(id(lise))    

#list are mutable objects


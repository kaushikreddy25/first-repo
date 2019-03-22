'''
Created on 09-Mar-2019

@author: guruk
'''

def person(name,age=18):
    print(name)
    print(age-2)
    
person(age= 25, name= 'Kaushik')

person('Kumar')

print('------------------------')
#keyword variable length argument
def person1(name,**data):
    print('Name: ', name)
    for i,j in data.items():
        print(i,':',j)
    
person1('Kaushik', Age= 25, Mob_No= 82932163, City= 'Ballari')


print('------------------------')
#variable length arguments
def sumk(a,*b):
    c= a
    for i in b:
        c = c+i
    print(c)
    
sumk(5,7,3,88,32,5.9,1.1)

print('------------------------')
def sum1(*b):
    c= 0
    for i in b:
        c = c+i
    print(c)
    
sum1(5,7,3,88,32,5.9,1.1)
'''
Created on 08-Feb-2019

@author: guruk
'''
num = 4+6j
print(type(num))
print('\n')

a= 6.87
b= int(a)
print(type(b))
c= float(b)
print(type(c))
print(c)
co= complex(b,9)
print(co)
print('\n')

k=10
print(b<k)
print(int(True))
print(int(False))
print(type(True))
print('\n')

print(range(5))
print(list(range(5)))
print('-----')
print(list(range(0,11,2)))#range can take three parameters
print(type(range(5)))
print('\n')
#tuple,set,list, range, string come under sequence

d= {'Kaushik':'Samsung Note', 'Ram':'iPhone', 'Naveen':'Mi 5'}
print(type(d))
print(d)
print(d.get('Kaushik'))
print(d.keys())
print(d.values())
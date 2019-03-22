'''
Created on 08-Feb-2019

@author: guruk
'''
from sys import getsizeof
from itertools import chain
'''To demo input() function to accept user input. It accepts string arguments'''

l = int(input('Enter length: '))
b = int(input('Enter Breadth: '))
area = l*b
print('Area of Rectangle is ', area)

print('-------------------------')

i = int(input('Enter integer value '))
f= float(input('Enter float value'))
print(i+f)
print('-------------------------')

print(eval('134')) #eval() takes string as a parameter
eval('print("hello")')
f= eval(input("Enter an expression"))
print(f)

print('-------------------------')
'''here we don't need to use '' for eval() because we aren't trying to print 
something like above ex. rather the input is automatically read as a string'''

j = eval(input('Enter any value '))
k= eval(input('Enter any value'))
print(j+k)

print('-------------------------')

r= eval( input('Enter the radius '))
ar = 3.14*r*r
print('Area of the circle is ', format(ar, '>10.3f')) #right justification in width 10
print(getsizeof(ar))

print(format('I am learning Python','>30s'))
print(format(0.31467,'20.2%'))
print(format(0.31467,'10.2%'))
print(format(3451.467,'10.3e'))

print('-------------------------')

print(max(2,3,4.5,5,0,6,7,8,9,6))
print(min(-9,2,3,4.5,5,6,7,8,9,6))
print(pow(3, 3))
print(pow(3, 3, 3))                 #3**3%3
print(round(67.65371, 3))
print(round(67.65321))

print('-------------------------')

print(ord('K'))
print(chr(99))

print('-------------------------')

ch = input("Enter a character")
print(ch[0])
print(ch)
print('\n')
cha = input('Enter a character')[0]
print(cha)
print(cha)




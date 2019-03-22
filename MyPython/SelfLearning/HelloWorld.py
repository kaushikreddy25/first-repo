'''
Created on 02-Feb-2019

@author: guruk
'''
print("Hello World, I am Python")

print('Hello',end='')
print(' Python',end='')
print(' I am Kaushik ')

print('------------')
print(2+3)
print(5/2)
print(5//2)

print(2*2*2)
print(2**3)

print('Kaushik\'s Laptop') #backslash ignores the inbuilt special meaning

print(r'C:\s\nikhil') #r = raw string. doesn't check for special operators like \n

x=9
y=3
print(x+y)
print('Before swapping values are ')
print(x)
print(y)
x,y = y,x
print('After swapping using multiple assignment')
print('x= '+ str(x)) #concatenation only for two strings
print('y=', y) 
print('\n')

name = 'Kaushik'
print(name)

print(name[6])
print(name[-1])

print('\n' + name[0:4]) #slicing

print(len(name))

print('Hello '+ name)

a=10
print(id(a))
print('\n')

b=10
print(id(b))
print('\n')

print(id(10))
print('\n')

k=10
print(id(k))

'''Python stores values and assigns tags(variables) to it. this way multiple
variables are pointing or tagged to a single address. that means value is 
more important than the name of the variable. this way Python saves space'''

print('\n')
h=36.24
print(type(h))
print(type(name))

























'''
Created on 12-Feb-2019

@author: guruk
'''
x= eval(input('Enter a number'))
r = x % 2

if r==1:
    print("Number is odd")
    
elif x==0:
        print('Number is 0')
else:
        print('Number is even')

print('-------------------------')

x=int(input("Enter a number"))
y=int(input("Enter a number"))
z=int(input("Enter a number"))

if x>y:
    if y>z:
        print("1st number is greatest")
    else:
        print('1st number is not greatest')
elif y<z:
    print("1st number is smaller than other two numbers")
else:
    print('1st number is not greatest')
    
print('-------------------------') 

print("Conditional expression Example")

t=int(input("Enter a number"))
t=t*t if t%2==0 else t*t*t
print("t = ", t)




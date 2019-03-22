'''
Created on 09-Mar-2019

@author: guruk
'''
x = int(input('Enter the number you want the factorial of-'))

def fact(k):
    f=1
    for i in range(1,k+1):
        f= f*i
    return f

res = fact(x)
print('Factorial of {} is {}'.format(x, res))

print('------------------------------------')

y = int(input('Enter the number you want the factorial of-'))

def factr(g):
    if g==0:
        return 1
    else:
        return g * factr(g-1)

res = factr(y)
print('Factorial is ', res)
        
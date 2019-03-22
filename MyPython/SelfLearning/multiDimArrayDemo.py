'''
Created on 05-Mar-2019

@author: guruk
'''
from numpy import *
from builtins import int
from cmath import sin


arr = array([12,3,43,34,56])

print(arr)

print('----------------------')

#outer limit is include unlike in range function
ar= linspace(0, 20, 3)

print(ar)

print('----------------------')

ar2 = arange(0,10,2)

print(ar2)

print('----------------------')

ar3 = logspace(2, 15, 5)

print('%.2f' %ar3[0])

print('----------------------')

ar4 = zeros(5, int)

print(ar4)

ar5 = ones(5, int)
print(ar5) 

print('----------------------')

arr2 = array([2,4,9,5])
arr3 = array([6,9,3,1])
arrs = arr2 + 1
arrs2 = arr2 + arr3
print(arrs)
print(arrs2)
print(sqrt(arr2))
print(sin(arr2[2]))
print(log(arr2))
print(min(arr2))
print(max(arr2))
print('----------------------')

print(concatenate([arr2,arr3]))
print('----------------------')
arrn = arr2
print(arrn)

print(id(arrn))
print(id(arr2))

print('----------------------')
#shallow copy\
arrn1 = arr2.view()
arr2[2] = 3

print(arrn1)
print(arr2)

print('----------------------')
#deep copy
arrn2 = arr3.copy()
arr3[2] = 5

print(arrn2)
print(arr3)

print('---------------------')

arr6 = array    ([  
                    [1,3,5,7,9],
                    [2,4,6,8,0]
       
                ])

print(arr6)
print(arr6.size)

print(arr6.ndim)

m = matrix(arr6)
print(m)

m1 = matrix('1,2,3 ; 4,6,7; 9,0,5')
m2 = matrix('8,9,6 ; 2,8,1; 2,7,3')
print(m1)

print(diagonal(m1))
print(m1.min())

m3 = m1 + m2
print(m3)

m4 = m1 * m2
print(m4)





'''
Created on 02-Mar-2019

@author: guruk
'''
from array import *
from builtins import int

arr = array('i', [])

n = int(input('Enter number of elements in array'))

for i in range(n):
    x= int(input("Enter value to add to array"))
    arr.append(x)
    
print(arr)

e = int(input('Enter number to search in array'))

k=0
for j in arr:
    if j==e:
        print('at index ', k)
        break
    k=k+1

#alternatively using functions
print(arr.index(e))

#removing element in index number 2 without inbuilt function
newarr = array(arr.typecode, [])
for i in range(len(arr)): #for i in arr: if i == arr[2] continue else: newarr.append(i)
    if i==2:
        continue
    else:
        newarr.append(arr[i])
print(newarr)
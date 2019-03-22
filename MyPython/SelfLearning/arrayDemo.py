'''
Created on 01-Mar-2019

@author: guruk
'''
from array import *

val = array('i',[3,4,1,7,89,6])
print(val)
print(val.buffer_info())
val.reverse()
print(val)
val.append(5)
print(val)
val.remove(89)
print(val)
val.reverse()
print(val)

print(val[1])

print("Printing all values: ")

for i in range(len(val)):
    print(val[i])
    
print("Printing all values again using diff. syntax: ")

for x in val:
    print(x)

print("Copying square of array elements into new array")

newVal = array(val.typecode,(a*a for a in val))

for j in range(len(newVal)):
    print(newVal[j])
'''
Created on 05-Feb-2019

@author: guruk
'''
#Lists can hold values of different data types. it can hold other lists as well.

from pkg_resources.extern import names
from pip._vendor.pyparsing import nums

nums = [20,12,17.8,58]
print(nums)
print('\n')

names = ['Dravid','Vicky','Raj','Kaushik']
print(names)
print('\n')

values= [nums,names]
print(values)
print('\n')

nums.insert(3,38)
print(nums)
print('\n')

nums.remove(58)
nums.append(79)
print(nums)
print('\n')

nums.pop(1) #removes based on index
print(nums)
print('\n')

del nums[2:]
print(nums)
print('\n')

nums.extend([36,88,84]) #note the syntax
print(nums)
print('\n')

print(min(nums))
print(max(nums))
print(sum(nums))
print('\n')

nums.sort()
print(nums)





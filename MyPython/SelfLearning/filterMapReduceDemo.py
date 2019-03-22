'''
Created on 11-Mar-2019

@author: guruk
'''
from functools import reduce


nums = [2,3,4,5,6,7,9,8]

evens = list(filter(lambda n : n%2==0, nums))

print(evens)

doubles = list(map(lambda d :d*2, evens))

print(doubles)

sums = reduce(lambda a,b : a+b, doubles)

print(sums)

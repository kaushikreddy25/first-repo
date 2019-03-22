'''
Created on 05-Feb-2019

@author: guruk
'''

#Tuple is immutable. can't change elements
tup = (12,13,45,78,43)
print(tup[3])

#set doesn't have index. doesn't allow duplicate values
set = {12,54,70,36}

print(set)
print(set.pop())
print(set)
print('\n')

print(set.__sizeof__())

#help(list)

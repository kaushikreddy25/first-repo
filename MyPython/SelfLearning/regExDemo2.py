'''
Created on 25-Mar-2019

@author: guruk
'''
#findall method and character classes

import re

#findall method doesnt't return match objects

str1 = "The rain in Spain and Portugal. India has ph no- 091-9876543231, 091-4563457896"
lyrics = ''' 12 Drummers Drumming
11 Pipers Piping
10 Lords a Leaping
9 Ladies Dancing
8 Maids a Milking
7 Swans a Swimming
6 Geese a Laying
5 Golden Rings
4 Calling Birds
3 French Hens
2 Turtle Doves
and 1 Partridge in a Pear Tree
'''


#Check if "Portugal" is in the string:

x = re.findall("Portugal", str1)
print(x)

if (x):
    print("Yes, there is at least one match!")
else:
    print("No match")
    
print('----------------------------')
# If 0 or 1 group, findall method returns list of strings
# if two or more groups, findall method returns list of tuples of strings.

phoneRegEx = re.compile(r'\d\d\d-\d\d\d\d\d\d\d\d\d\d')
print(phoneRegEx.findall(str1))

print('If two or more groups-------')

phoneRegEx = re.compile(r'((\d\d\d)-(\d\d\d\d\d\d\d\d\d\d))')
print(phoneRegEx.findall(str1))

print('--------------------')

xmasRegEx = re.compile(r'\d+\s\w+')
print(xmasRegEx.findall(lyrics))

print('----------------------')
#making our own character class

vowelRegEx = re.compile(r'[aeiouAEIOU]') # r'(a|e|i|o|u')
print(vowelRegEx.findall(str1))
print('Double vowel check-------')
doublevowelRegEx = re.compile(r'[aeiouAEIOU]{2}') 
print(doublevowelRegEx.findall(str1))
print('Negative character class check-------') #finds everything other than what's in the character class
consonantRegEx = re.compile(r'[^aeiouAEIOU]') 
print(consonantRegEx.findall(str1))

print('Ignorecase---------')

ignorecaseRegEx = re.compile(r'[aeiou]',re.I)
print(ignorecaseRegEx.findall(str1))

#https://1drv.ms/u/s!Amv7MQc0Jhpislq13qy-T2mCgvNo


'''
Created on 25-Mar-2019

@author: guruk
'''
import re

phoneNumRegEx = re.compile(r'\d\d\d-\d\d\d\d\d\d\d\d\d\d')
print('Found these numbers in given text - ', phoneNumRegEx.findall("Call me at 091-8826654628 or at 091-1234567890"))

print('-----------------')

pn = input("Enter the message to check for an \nIndian mobile number with country code in the format 091-XXXXXXXXXX : ")
regEx = re.compile(r'(\d\d\d)-(\d\d\d\d\d\d\d\d\d\d)')
mo = regEx.search(pn)
print('Country code is - ', mo.group(1))

print('Phone number is - ', mo.group(2))

print('-----------------------------')

#Pipe character | is used to seperate different groups while searching for patterns.
regEx1 = re.compile(r'bat(man|mobile)')
mo = regEx1.search('batman has a batmobile')
print(mo.group())
print(mo.group(1))
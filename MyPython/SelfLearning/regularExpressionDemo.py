'''
Created on 25-Mar-2019

@author: guruk
'''
import re

phoneNumRegEx = re.compile(r'\d\d\d-\d\d\d\d\d\d\d\d\d\d')
print('Found these numbers in given text - \n ', phoneNumRegEx.findall("Call me at 091-8826654628 or at 091-1234567890"))

print('-----------------')

pn = input("Enter the message to check for an \nIndian mobile number with country code in the format 091-XXXXXXXXXX : ")
regEx = re.compile(r'(\d\d\d)-(\d\d\d\d\d\d\d\d\d\d)')
mo = regEx.search(pn)
if mo == None:
    print('Not found')
else:    
    print('Country code is - ', mo.group(1))
    print('Phone number is - ', mo.group(2))

print('-----------------------------')

#Pipe character | is used to seperate different groups while searching for patterns.
regEx1 = re.compile(r'bat(man|mobile)')
mo = regEx1.search('batman has a batmobile')
print(mo.group())
print(mo.group(1))

print('-------------------------------')
#'?' is used to make a group optional. that particular group can occur 
#zero or one time. Like country code in this example.
regEx2 = re.compile(r'(\d\d\d-)?\d\d\d\d\d\d\d\d\d\d')
mo = regEx2.search('My number is 8826654628. Do call me')
print(mo.group())

print('-------------------------------')
#'*' is used to make a group optional. that particular group can occur 
#zero or more times. 'wo'in this group can occur zero times = batman or multiple times
regEx3 = re.compile(r'bat(wo)*man')
mo = regEx3.search('The adventures of batman.')
print(mo.group())
mo = regEx3.search('The adventures of batwowoman')
print(mo.group())

print('---------------------------')

#'+' is used to make a group optional. that particular group can occur 
#one or more times. So here batman wont be recognized coz wo is zero times in batman.
regEx4 = re.compile(r'bat(wo)+man')
mo = regEx4.search('The adventures of batman')
if mo == None:
    print("Not Found")
mo = regEx4.search('The adventures of batwowoman')
print(mo.group())

print('---------------------------')

regEx5 = re.compile(r'((\d\d\d-)?\d\d\d\d\d\d\d\d\d\d(,)?){3}')
mo = regEx5.search('My numbers are 091-8826654628,1234567890,0987667890 . Do call me')
print(mo.group())

print('------------------------------')
#check if a particular pattern appears a certain number of times within a range
#here can be one time or upto three times

regEx6 = re.compile(r'((\d\d\d-)?\d\d\d\d\d\d\d\d\d\d(,)?){1,3}')
mo = regEx6.search('My numbers are 091-8826654628,1234567890,0987667890 . Do call me')
print(mo.group())
mo = regEx6.search('My number is 8829994646 . call me')
print(mo.group())

print('----------------------')
#Greedy and non-greedy match

digitregEx = re.compile(r'(\d){3,5}')
mo = digitregEx.search("Here are 12345678")
print(mo.group())

digitregEx1 = re.compile(r'(\d){3,5}?')
mo = digitregEx1.search("Here are 12345678")
print(mo.group())

# Review - https://1drv.ms/u/s!Amv7MQc0JhpislU4xjPiWsSIxln5












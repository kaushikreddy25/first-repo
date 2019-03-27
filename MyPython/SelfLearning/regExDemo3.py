'''
Created on 27-Mar-2019

@author: guruk
'''
#Lesson 27 of Automate the boring stuff

import re

#'^' used outside character class to indicate use of the following text at the 
#beginning of the search string

startRegEx = re.compile(r'^Hello')
mo = startRegEx.search("Hello amazing World") 
if mo == None:
    print('Nothing Found')
else:
    print(mo.group())

print('Case 2---')
mo = startRegEx.search("I am Python, Hello amazing World") 
if mo == None:
    print('Nothing Found')
else:
    print(mo.group())
    
print('-----------------')

#'$' used outside character class to indicate use of the following text at the 
#end of the search string. Will return None if found elsewhere in string.

endRegEx = re.compile(r'World$')
mo = endRegEx.search("Hello amazing World") 
if mo == None:
    print('Nothing Found')
else:
    print(mo.group())

print('Case 2---')
mo = endRegEx.search("Hello amazing World, I am python") 
if mo == None:
    print('Nothing Found')
else:
    print(mo.group())
    
print('------------------')    
#has to begin and end with that given pattern

startendRegEx = re.compile(r'^\d+$')
mo = startendRegEx.search("987654125433") 
if mo == None:
    print('Nothing Found')
else:
    print(mo.group())

print('Case 2---')
mo = startendRegEx.search("98765 54325") 
if mo == None:
    print('Nothing Found')
else:
    print(mo.group())
print('-------------------')
# '.' means anything except newline

anyRegEx = re.compile(r'.{3}e')
print(anyRegEx.findall('The rage is of that i saw the face of dog in a cage was a lot.'))

# '.*' means anything except newline zero or more times

lanyRegEx = re.compile(r'First Name: (.*) Last Name: (.*)')
print(lanyRegEx.findall('First Name: Kaushik Last Name: Reddy'))

# '.*?' non greedy anything

nglanyRegEx = re.compile(r'<.*?>')
print(nglanyRegEx.findall('<Hello> I am Kaushik>'))

print('Greedy case---')
glanyregEx = re.compile(r'<.*>')
print(glanyregEx.findall('<Hello> I am Kaushik>'))


#https://1drv.ms/u/s!Amv7MQc0Jhpislvnpv-ImQQ67oCm

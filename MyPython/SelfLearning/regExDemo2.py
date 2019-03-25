'''
Created on 25-Mar-2019

@author: guruk
'''
import re

str1 = "The rain in Spain and Portugal"

#Check if "Portugal" is in the string:

x = re.findall("Portugal", str1)
print(x)

if (x):
    print("Yes, there is at least one match!")
else:
    print("No match")
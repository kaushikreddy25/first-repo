'''
Created on 27-Mar-2019

@author: guruk
'''
# Find and sub method, Verbose mode

import re

subregEx = re.compile(r'Agent \w+')
#print(subregEx.findall("Agent Kaushik gave Agent Bond some documents"))
print(subregEx.sub('Agent ****', "Agent Kaushik gave Agent Bond some documents"))

subregEx1 = re.compile(r'Agent (\w)\w+')
print(subregEx1.sub(r'Agent \1***', "Agent Kaushik gave Agent Bond some documents"))


print('----------------------------')
# Verbose mode 're.X' gives documentation abilities in regular Exps. for easy comprehension
#ignores all whitespaces

numregEx = re.compile(r'''
(
((\d\d\d-)|            #country code in 091- format
(\+\d\d(\s)?))?            #country code in +91 format
\d\d\d\d\d                #first five digits
\d\d\d\d\d                #last five digits
)            
''',re.X)
alltuples = numregEx.findall('My numbers are 091-9926654628 , +91 8826654628 , 8826654628 ')
phonenums = []
for i in alltuples:
    phonenums.append(i[0])
    
print(phonenums)

#Verbose works despite error being shown. how to print everything when we use groups?
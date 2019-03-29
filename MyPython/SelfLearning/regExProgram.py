'''
Created on 29-Mar-2019

@author: guruk
'''
import re, pyperclip


# TODO - Create a Regex object for phone numbers

phoNumRegEx = re.compile(r'''
(
((\d\d\d-)|            #country code in 091- format or city telephone code for landlines (OPTIONAL)
(\+\d\d(\s)?))?            #country code in +91 format (OPTIONAL)
\d\d\d\d\d                #first five digits
\d\d\d(\d\d)?                #last three or five digits
)            
''',re.X)


# TODO - Create a Regex for email IDs

emailRegEx = re.compile(r'''
#some.+_thing@some.+_thing.com
(
[a-zA-Z.+_]+            #username part
@                        #@ part
[a-zA-Z.+_]+            #domain part
)
''', re.X)

# TODO - Get the text off the clip-board
text = pyperclip.paste()


# TODO - Extract the phone numbers and email IDs

extractedPhoneNums = phoNumRegEx.findall(text)
phonenums = []
for i in extractedPhoneNums:
    phonenums.append(i[0])


extractedEmailss = emailRegEx.findall(text)

# TODO - Send the text found to clip-board for pasting elsewhere

results = '\n'.join(phonenums) + '\n' + '\n'.join(extractedEmailss)
pyperclip.copy(results)


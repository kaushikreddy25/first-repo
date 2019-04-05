'''
Created on 05-Apr-2019

@author: guruk
'''
#Lesson 038

#Searching on youtube from clipboard.
#! python3
import webbrowser, pyperclip, sys

#search = pyperclip.paste()

webbrowser.open('https://www.youtube.com/results?search_query=' + search)

print('--------------------')

if len(sys.argv) > 1:
    address = ''.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/'+ address)
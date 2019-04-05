'''
Created on 29-Mar-2019

@author: guruk
'''
import os

filen = 'mydata.txt'
print('Join path >>>')
print(os.path.join('folder1','folder2 in folder1','folder3 in folder2','samsung.jpeg -in folder3-'))
print(os.path.join('W:\\Python\\Programs',filen))
print()
print('Current working directory >>>')
print(os.getcwd())
print()
print('Change Directory>>> ')
os.chdir('W:\\Python\\Automate the Boring Stuff with Python Programming - Udemy')

print(os.getcwd())

print('Absolute Path----')
file1 = os.path.abspath('Files1.png')
print(file1)

print('Dir NAme ----')
print(os.path.dirname(file1))
print('Base name----')
print(os.path.basename(file1))

print('To check if a file exists on hard drive---')
print(os.path.exists(file1))
print(os.path.exists('W:\\Python\\Programs\\Helloworld.py'))
print('To get file size in bytes---')
print(os.path.getsize('W:\\Jobs\\CV.docx'))

print('To list all files in a folder---')
print(os.listdir('W:\\Jobs'))

print('--------------------------')
# TODO - To find the total size of all files in a folder.

totalsize = 0

for file in os.listdir('W:\\Jobs'):
    print('Printing name of file >>> ',file)
    if os.path.isfile(os.path.join('W:\\Jobs',file)):
        totalsize = totalsize + os.path.getsize(os.path.join('W:\\Jobs',file))
    else:
        continue

print("Total size is: ",totalsize)


#https://1drv.ms/u/s!Amv7MQc0JhpislyDudLxv4s12iYB
#https://1drv.ms/u/s!Amv7MQc0Jhpisl0PLJoPxyucdChA
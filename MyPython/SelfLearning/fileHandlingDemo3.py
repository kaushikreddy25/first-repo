'''
Created on 04-Apr-2019

@author: guruk
'''
#Video 032 - Automate the boring stuff

import shutil

shutil.copy('W:\\Python\\testDoc.txt', 'W:\\Python\\Programs')

shutil.copy('W:\\Python\\testDoc.txt', 'W:\\Python\\Programs\\copiedfile.txt')
shutil.copytree('W:\\Python\\Programs\\tobecopied','W:\\Python\\tobecopied_backup')

#make sure file exists after running program once
shutil.move('W:\\Python\\movetestdoc.txt','W:\\Python\\Programs')

#rename file using move function
shutil.move('W:\\Python\\renametoRename.txt','W:\\Python\\Rename.txt')

#shutil.move('W:\\Python\\Rename.txt','W:\\Python\\renametoRename.txt')

import os

os.chdir('W:\\Python\\Programs')

for filename in os.listdir():
    if filename.endswith('.txt'):
        shutil.copy(filename, 'W:\\Python\\Programs\\checktxtcopy')

#Deleting files- Lesson 033 - Recap>
#https://1drv.ms/u/s!Amv7MQc0Jhpisl-ePyPRlHFTocP1
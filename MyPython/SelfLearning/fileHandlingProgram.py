'''
Created on 04-Apr-2019

@author: guruk
'''
import os

# Walk through all files n folders in a folder. to be used with for loop. 
#returns three variables 

for folderName, subFolders, fileNames in os.walk('W:\\Python\\Programs'):
    print('The folder is ', folderName)
    print('The subfolders in '+ folderName + ' are ' + str(subFolders) )
    print('The files in '+ folderName + ' are ' + str(fileNames) )
    print()
    
    for subfol in subFolders:
        print(subfol)
        if 'againcheck' in subfol:
            print("I am checking again....")
            
    for filena in fileNames:
        print(filena)
        if filena.endswith('.txt'):
            print("-------This is a text file")
        else:
            print('-------This isn\'t a text file')
        
         
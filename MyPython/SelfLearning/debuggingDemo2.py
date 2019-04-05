'''
Created on 05-Apr-2019

@author: guruk
'''
#Lesson 035

import traceback

def Boxprint(symbol,height, width):
    if len(symbol) != 1:
        try:
            raise Exception('Symbol should be 1 character long.')
        except:
            errorFile = open('ErrorFile.txt','a')
            errorFile.write(traceback.format_exc())
            errorFile.close()
            print("Error is now handled and logged." )
      
    if height < 2 or width < 2:
        try:    
            raise Exception('Height and width should be greater than 2')
        except:
            errorFile = open('ErrorFile.txt','a')
            errorFile.write(traceback.format_exc())
            errorFile.close()
            print("Error is now handled and logged." )
    
    if len(symbol) == 1:
        print(symbol * width)
    
    
        for i in range(height-2):
            print(symbol + (' '* (width-2)) + symbol)
        
        print(symbol* width)
    else:
        pass
    
Boxprint('#', 5, 10)

print('Case 2 > ')
Boxprint('OO', 10,5)

print('Case 3 > ')

Boxprint("*", 1 ,1)



print('----------------')

g_nagar = {'ns': 'green','ew':'red'}


def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'
    
    assert 'red' in intersection.values(), 'Neither light is red!!!'
    
    print(intersection)

switchLights(g_nagar)  

# after runnning this program we see traffic is running in both directions
# as both lights are now switched to yellow and green. this shouldn't happen
# one light should atleast be red. so we use assert statement.
# if assert condition is false, program will crash
# assert used for programming errors while try-except for user errors.



#https://1drv.ms/u/s!Amv7MQc0JhpismCeasEbwgufoAOd


'''
Created on 20-Mar-2019

@author: guruk
'''
pos = -1

def search(lst,num):
    k=0
    for i in lst:
        
        if i== num:
            globals()['pos'] = k
            return True
        k+=1
    return False


lst = [1,3,5,7,9]
num = int(input('Enter single digit number to search'))


if search(lst,num):
    print("Found at {} position".format(pos+1))
else:
    print("Number not found in the list")




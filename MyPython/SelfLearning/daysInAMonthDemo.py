'''
Created on 23-Feb-2019

@author: guruk
'''

h=1
while h==1:
    x= int(input("Enter the month in numerical ex: 2 for February"))
    if x<=12:
        if x==2:
            y= int(input("Enter Year"))
            if y%4==0:
                print("Number of days is 29")
            else:
                print("Number of days is 28")
        elif x in (1,3,5,7,8,10,12):
            print("Number of days in month is 31")
        elif x in (4,6,9,11):
            print("Number of days is 30")
        h=2        
    else:
        print("Invalid input. Try again")
'''
Created on 23-Feb-2019

@author: guruk
'''
n= int(input("Enter a number"))
x= n
for i in range(2,n):
    if x%i==0:
        #print("Number not prime")
        flag=1
        break
        
    else:
        #print("Number is prime")
        flag=0
    
if flag==1:
    print("Number not prime")
else:
    print("Number is prime")
    
        
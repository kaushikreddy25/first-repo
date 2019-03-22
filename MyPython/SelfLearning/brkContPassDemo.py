'''
Created on 22-Feb-2019

@author: guruk
'''
from builtins import int
av=10
x=int(input("How many chocolates do you want?"))
i=1

while i <=x:
    if i>av:
        print("Sorry, We only have ", av, " Chocolates available")
        break
    
    print("Here's a chocolate")
    i+=1

print("Transaction complete")

print('-------------------------')

#skip divisible by number in a range

p = int(input("Enter number to skip"))
for j in range(1,51):
    if j%p ==0:
        continue
    print(j)
        
print("This is printed because continue only skips that particular loop. This is outside for loop")

print('-------------------------')

for k in range(1,51):
    if(k%2==0):
        pass
    else:
        print(k)
    
'''
Created on 26-Feb-2019

@author: guruk
'''
for i in range(5): 
    for j in range(5):
        print('# ', end ="")
    
    print()  

print('-------------------------')

for i in range(1,6): 
    for j in range(i):
        print('# ', end ="")
    
    print()  

print('-------------------------')

for i in range(5): 
    for j in range(5-i):
        print('# ', end ="")
    
    print()  
    
print('-------------------------')

for i in range(1,5): 
    for j in range(5-i):
        print(j+i ," ", end ="")
    
    print()  
print('-------------------------')

for i in range(4): 
    for j in range(4):
        if i>=j:
            print(chr(65+j)," ", end ="")
        else:
            print(chr(79+j)," ", end="")    
    
    print()  

print('-------------------------')



'''
Created on 09-Mar-2019

@author: guruk
'''
a = 15                                  #Global Variable
def update():
    a= 10                               #Local Variable
    print('Inside function ' ,a)
    
update()
print('Outside function ', a)

print('------------------------')

c = 15                                  #Global Variable
def update2():
                                           
    print('Inside function ' ,c)        #No Local Variable
    
update2()
print('Outside function ', c)
'''
Means function can access global variable but outside can't access local variable
function gives preference to local variable in case of conflict.
'''
print('------------------------')

b = 15                                  #Global Variable
def update1():
    global b
    b= 10                               #Global Variable
    print('Inside function ' ,b)
    
update1()
print('Outside function ', b)
print('------------------------')
'''
Using global and local variables in same function
'''

d = 15  
print(id(d))                               
def update4():
    d= 10                             
    globals()['d']= 20
    print('Inside function ' ,d)
''' 
    x = globals()['d']
    print(id(x))
'''   
    
    
          
update4()
print('Outside function ', d)


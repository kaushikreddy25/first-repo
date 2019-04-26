'''
Created on 20-Apr-2019

@author: guruk
'''
#!python 3

#To demo the use of self-parameter with instance variable
#to demo use of self to call one function from inside another in same class

class Prac:
    x=5
    def disp(self,x):
        x=30
        print('In first display function')
        print('The value of local variable is', x)
        print('The value of instance variable is', self.x)
    
    def disp2(self):
        self.disp(20)
        print('In 2nd display function')
class B:
    pass

     
ob = Prac()
ob.disp2()
print(dir(Prac))
print(Prac.__dict__)
print(Prac.__class__)
ob2 = B()

print(isinstance(ob,Prac))
print(isinstance(ob2,B))
print(isinstance(ob,B))
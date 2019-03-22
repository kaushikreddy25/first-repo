'''
Created on 19-Mar-2019

@author: guruk
'''
class A:
    
    def show(self):
        print("In A Show ")
        
class B(A):
    
    def show(self):
        print('In B Show ')
        
o1 = B()
o1.show()
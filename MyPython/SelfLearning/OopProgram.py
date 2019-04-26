'''
Created on 26-Apr-2019

@author: guruk
'''
#! python 3

#Program to perform mathematical ops on complex numbers

class Complex:
        
    def __init__(self,r,i):
        self.real = r
        self.imag = i
    
    def display(self):
        print('Complex number is ', self.real, ',',self.imag)
    
    def __add__(self,other):
        return complex(self.real+other.real,self.imag+other.imag)
    
    def __sub__(self,other):
        return complex(self.real-other.real,self.imag-other.imag)
    
    def __mul__(self,other):
        return complex((self.real*other.real)-(self.imag*other.imag),(self.real*other.imag)+(self.imag*other.real))
    
    def __eq__(self,other):
        if self.real == other.real and self.imag== other.imag:
            return True
        else:
            return False 
    
    def __le__(self,other):
        if self.real < other.real and self.imag < other.imag:
            return True
        else:
            return False 
        
    def __ge__(self,other):
        if self.real > other.real and self.imag > other.imag:
            return True
        else:
            return False 
    
    
    
c1 = Complex(3,2)
c2 = Complex(2,1)

c3 = c1 + c2
print('Addition: ', c3)

c4 = c1-c2
c5 = c1*c2
print('Subtraction: ',c4)
print('Multiplication: ',c5)

print('Checking equality: ', c1==c2)
print('Is c1 greater than c2? ',c1>=c2)
print('Is c1 lesser than c2? ', c1<=c2)






    
'''
Created on 16-Mar-2019

@author: guruk
'''
class A:
    
    def feature1(self):
        print('A - Feature 1 is working')
    
    def feature2(self):
        print('A - Feature 2 is working')
    
class B(A):
    
    def feature3(self):
        print('B - Feature 3 is working')
        
    def feature4(self):
        print('B- Feature 4 is working')
        
class C(B):
    
    def __init__(self):
        print('in class C which inherits B which in-turn inherits A')
        
    def feature5(self):
        print('C- Feature 5 is working')

class D:
    def feature6(self):
        print('D- Feature 6 is working')
       
class E(A,D):
    
    def __init__(self):
        print('in class E which inherits A and D')
    
    def feature7(self):
        print('E- Feature 7 is working')

#Multilevel inheritance        

c1 = C()
c1.feature1()


print()
print('------------')
print()
#Multiple inheritance

e1 = E()
e1.feature1()
e1.feature6()

'''
if you create object of sub class it will first try to find init of sub class
only if it is not found it will call init of super class. 
'''
print('-------------------------')

print()

class G:
    
    def __init__(self):
        print('in class G init ')
        
    def feature9(self):
        print('G- Feature 9 is working')

class H:
    
    def __init__(self):
        print(' in class H init')
    
    def feature10(self):
        print('H- Feature 10 is working')
       
class I(H,G):
    
    def __init__(self):
        super().__init__()
        print('in class I init which inherits G and H')
    
    def feature11(self):
        print('I- Feature 11 is working')

i1 = I()
i1.feature9()
i1.feature10()

'''
MRO - when calling super and there are 2 super classes(Multiple Inheritance)
then first priority is given from LEft to Right
'''












    
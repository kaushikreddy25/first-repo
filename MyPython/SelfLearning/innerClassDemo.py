'''
Created on 16-Mar-2019

@author: guruk
'''

class human:
        
    def __init__(self,nm,cty, comp, colour):
        self.name = nm
        self.city = cty
        self.pho = self.phone(comp, colour)
        
    def show(self):
        print(self.name,self.city)
        self.pho.show()
        
    class phone:
        
        def __init__(self,comp, colour):
            self.com = comp
            self.col = colour
                
        def show(self):
            print(self.com, self.col)

        
h1 = human('Kaushik', 'Ballari', 'Samsung', 'Black')
phone1 = h1.pho
h1.show()

'''
when there is inner class. create its object variable in __init__ of outer class.
Use this object variable to call methods of inner class 
'''
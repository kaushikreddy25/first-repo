'''
Created on 12-Mar-2019

@author: guruk
'''
class computer:
    
    screen = 15.6
    
    def __init__(self):
        self.name = "Lenovo"
        self.ram = '16'
        
    def compare(self,other):
        if self.ram== other.ram:
            return True
        else: return False
    
    @classmethod
    def get_screen(cls):
        print('using Class method. The screen size of this computer is {} '.format(computer.screen))
        
    @staticmethod
    def info():
        print("This is static method (accepts no variables)- info")
        
        
c1 = computer()
c2 = computer()

c1.ram = 8


if c1.compare(c2):
    print("Same RAM")
else:
    print('Different RAM Size')
    
    
print(c1.ram)
print(c2.ram)
print(computer.screen)
print(c1.screen)
print(c2.screen)
computer.screen = 14.1
print(c1.screen)

computer.get_screen()

computer.info()





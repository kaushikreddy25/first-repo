'''
Created on 18-Mar-2019

@author: guruk
'''


class eclipse:
    
    def execute(self):
        print("Compiling")
        print("Executing")
        
class myEditor:
    
    def execute(self):
        print("Checking")
        print("Error Handling")
        print("Compiling")
        print("Executing")

class python:
    
    def run(self,ide):
        ide.execute()
        

ide1 = eclipse()
ide2 = myEditor()


py1 = python()
py1.run(ide1)
print()
py1.run(ide2)
                
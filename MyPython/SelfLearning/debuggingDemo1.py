'''
Created on 19-Mar-2019

@author: guruk
'''

a = int(input("Enter first number "))
c = int(input("Enter second number "))

try: 
    print("Resource opened ")
    
    print("Result: ", a/c)
    
except ZeroDivisionError as e:
    print('Don\'t divide by Zero')

except ValueError as e:
    print('Invalid input ')

except Exception as e:
    print('Something went wrong- ', e)

finally:
    print("Resource closed ")
    
'''
finally block will be executed if there is a error or not.
'''

print('-----------------------')

# Program to handle multiple errors with one except statement 
try : 
    d = int(input("Enter single digit number "))
    if d < 4 : 

        # throws ZeroDivisionError for a = 3 
        b = d/(d-3) 
    
    # throws NameError if a >= 4 
    print("Value of b = ", b) 

# note that braces () are necessary here for multiple exceptions 
except(ZeroDivisionError, NameError) as e: 
    print( "\nError Occurred-  {} -  and Handled. ".format(e))

print('-----------------------')
'''
you can also use else clause on try-except block which must be present
after all the except clauses. The code enters the else block only if 
the try clause does not raise an exception.
'''


# Program to depict else clause with try-except 

# Function which returns a/b 
def AbyB(x,y): 
    try: 
        g = ((x+y) / (x-y)) 
    
    except ZeroDivisionError: 
        print ("a/b result is 0")
    
    else: 
        print (g) 
        print('In else block')
        

# Driver program to test above function 
AbyB(2.0, 3.0)
print('Second example-> ') 
AbyB(3.0, 3.0) 

print('----------------------------------')

# Program to depict Raising Exception 

try: 
    raise NameError("Hi there") # Raise Error 

except NameError: 
    print ("An user raised exception")

    print('To check - ')
    raise # To determine whether the exception was raised or not 

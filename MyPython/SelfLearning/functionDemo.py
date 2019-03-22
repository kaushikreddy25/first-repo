def greet():
    print('Hello')
    print("Good morning")
    
greet()

def add(x,y):
    z= x+y
    print('added using function - ', z)

add(4, 2)

def subtract(x,y):
    z= x-y
    return z

res = subtract(4, 2)
print('subtracted using function - ',res)

def mul_divide(x,y):
    z= x*y
    a= x/y
    return z,a

r1,r2 = mul_divide(9, 3)
print('After multiplication and division - ',r1,r2)
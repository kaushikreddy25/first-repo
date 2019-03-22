a = 4
b = 6

print(a+b)
print('Behind the scenes -> ')

print(int.__add__(a,b))

print('------------Operator overloading now ----------')

class student:
    
    def __init__(self,m1,m2):
        self.m1= m1
        self.m2 = m2
        
    def __add__(self,other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        print(m1,m2)
    
    def __gt__(self,other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False
    
    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)        
    
    
s1 = student(45,90)
s2 = student(60,60)

s3 = s1 + s2

'''
Here we are overloading the inbuilt add operator.
Next we will overload greater than operator.
'''

if s1 > s2:
    print("Student 1 scores more")
else:
    print("Student 2 scores more")

print(s1.__str__())

print(s1)
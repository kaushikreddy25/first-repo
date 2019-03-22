'''
Created on 09-Mar-2019

@author: guruk
'''

input("Enter 10 numbers with space between 2 numbers")
a = [int(x) for x in input().split()]

def even_odd(k):
    print(k)
    e,o =0,0
    for i in k:
        if i%2==0:
            e+=1
        else:
            o+=1
    return e,o

even, odd = even_odd(a)
print('Number of even numbers in user inputed numbers: ',even)
print('Number of odd numbers in user inputed numbers: ',odd)

print('-----------------')


input("Enter first names with space between 2 names")
b = input().split()

def name_len(j):
    print(j)
    m5,l5=0,0
    for i in j:
        if len(i)>5:
            m5+=1
        else:
            l5+=1
    return m5,l5

mo5, lo5 = name_len(b)
print('Names with more than 5 letters : ',mo5)
print('Names with less than 5 letters: ',lo5)
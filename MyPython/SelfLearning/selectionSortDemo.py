'''
Created on 20-Mar-2019

@author: guruk
'''
from time import sleep

def sort(nums):
    for i in range(len(nums)):
        minpos = i
        for j in range(i+1 ,len(nums)):
            if nums[j] < nums[minpos]:
                minpos = j
                
        nums[i],nums[minpos]=nums[minpos],nums[i]

        
                
nums = [1,9,2,8,4,7,5, 22, 57, 43 ,97,16,70,35]
print('Unsorted list is - ', nums)
print("Sorting....")

sort(nums)
sleep(1)
print('Sorted list is - ', nums)


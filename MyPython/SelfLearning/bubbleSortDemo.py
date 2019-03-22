'''
Created on 20-Mar-2019

@author: guruk
'''
from time import sleep

def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]

nums = [1,9,2,8,4,7,5, 22, 57, 43 ,97,16,70,35]
print('Length of the list is ', len(nums))
print('Unsorted list is - ', nums)
print("Sorting....")

sort(nums)
sleep(1)
print('Sorted list is - ', nums)
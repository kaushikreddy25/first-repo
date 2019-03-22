pos = -1

def search(lst,num):
   
    l = 0
    u = len(lst)-1
    
    while l<=u: #for i in lst:
        mid = (l + u )//2
        if lst[mid] == num:
            globals()['pos'] = mid
            return True
        else:
            if lst[mid] <= num:
                l = mid+1
            else:
                u = mid-1
        
    return False

lst = [1,2,3,5,6,7,9]
num = int(input('Enter single digit number'))

if search(lst,num):
    print("Found at {} position".format(pos+1))
else:
    print("Number not found in the list")


# can't use counter here because searching isn't linear.
# needs a sorted list

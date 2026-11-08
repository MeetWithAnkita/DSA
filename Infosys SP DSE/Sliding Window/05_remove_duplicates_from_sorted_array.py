'''
Problem: Given a sorted integer array, remove duplicates 
in-place so that each unique element appears only once. 
Return the number of unique elements.
'''

nums = [1, 1, 2, 2, 3, 4, 4]

def remove_duplicates(arr):
    slow = 0 
    for fast in range(1, len(arr)):
        if arr[slow] != arr[fast]:
            slow += 1 
            arr[slow] = arr[fast]
    k = slow+1
    return k

C = remove_duplicates(nums)
print("Unique count: ",C)
print("Unique elements: ",nums[:C] )

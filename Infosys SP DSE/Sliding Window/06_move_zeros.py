'''
Given an integer array, move all zeroes to the end while 
maintaining the relative order of non-zero elements.
'''

nums = [0, 1, 0, 3, 12]
def move_zeros(arr):
    non_z = 0 
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[non_z], arr[i] = arr[i], arr[non_z] 
            non_z += 1
            
    return arr

print(move_zeros(nums))

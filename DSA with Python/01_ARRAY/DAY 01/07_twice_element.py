# Modify the array so that every element becomes twice its original value.
# Rules:
# Don't create a second array.
# Modify the original arr.
# Use a loop.

arr = [10, 20, 30, 40, 50]
for i, value in enumerate(arr):
    arr[i] = value * 2 
print(arr)
# time: O(n), space: O(1) 

# This is called in-place modification.
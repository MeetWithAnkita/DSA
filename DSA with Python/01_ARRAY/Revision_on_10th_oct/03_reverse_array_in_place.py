# [x] 3. Reverse an Array In-Place
# Reverse the array without using slicing or another array.
# arr = [1, 2, 3, 4, 5] → [5, 4, 3, 2, 1]
arr = [1, 2, 3, 4, 5]

left = 0 
right = len(arr) -1 
while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1 
    right -= 1 
print(arr)



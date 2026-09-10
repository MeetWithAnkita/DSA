arr = [1, 2, 3, 4, 5]
# Rotate the array one position to the right.
# expected output: 
# [5, 1, 2, 3, 4]
last = arr[len(arr) - 1]
for i in range(len(arr)-1, 0, -1 ):
    arr[i] = arr[i-1]
arr[0] = last
print(arr)

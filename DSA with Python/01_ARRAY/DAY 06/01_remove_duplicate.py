arr = [1, 2, 2, 2, 3, 4, 4, 5]
position = 0
# remove duplicates from sorted array 
while position < len(arr) -1:
    if arr[position] == arr[position + 1]:
        arr.pop(position + 1)
    else: 
        position += 1 

print(arr)

# Time: O(n)
# space: O(1)
# In place 
    




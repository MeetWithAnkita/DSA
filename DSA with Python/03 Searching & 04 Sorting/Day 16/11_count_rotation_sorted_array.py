# arr = [7, 9, 11, 1, 3, 5]
# arr = [1, 2, 3, 4, 5, 6] 
arr = [4, 5, 6, 1, 2, 3]

def count_rotation(arr):
    s = 0
    e = len(arr) - 1 
    while s < e:
        m = (s + e) // 2 
   
        if arr[m] > arr[e]:
            s = m + 1 
        else:
            e = m
    return s 

print(count_rotation(arr))

# Complexity
# - Time: O(log n)
# - Auxiliary Space: O(1)

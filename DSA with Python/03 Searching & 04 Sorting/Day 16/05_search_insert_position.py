# Important concept
# For Search Insert Position:
# - If the target exists → return its index.
# - If the target doesn't exist → return the index where it should be inserted.

# arr = [10, 20, 30, 40, 50]
# target = 35
arr = [5, 10, 15, 20, 25]
target = 2
def index_position(arr, target):
    s = 0 
    e = len(arr) - 1 
    while s <= e:
        m = (s+e) // 2 
        if target == arr[m]:
            return m
        elif target < arr[m]:
            e = m - 1 
        else:
            s = m + 1 
    return s
    
print(index_position(arr, target))


# Complexity:
# - Time: (O(log n)
# - Auxiliary Space: (O(1)
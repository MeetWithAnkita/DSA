# arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# target = 60
arr = [5, 15, 25, 35, 45, 55, 65]
target = 35
def binary_search(arr, target):
    length = len(arr)
    s = 0
    e = length - 1 

    while s <= e:
        m = (s + e) // 2 
        if arr[m] == target:
            return m
        elif arr[m] > target:
            e = m - 1 
        elif arr[m] < target:
            s = m + 1 
    return -1

print(binary_search(arr, target))


# Best-case time ==> (O(1)
# Average/worst-case time ==> O(log n)
# Auxiliary space (iterative) ==> (O(1)
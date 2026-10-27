# For ascending arrays:
# - If target < arr[m] → move left.
# - If target > arr[m] → move right.

# For descending arrays, the conditions are reversed:
# - If target < arr[m] → move right.
# - If target > arr[m] → move left.

arr = [90, 70, 50, 30, 10]
target = 30

def bs_desc(arr, target):
    s = 0 
    e = len(arr) - 1 
    while s <= e :
        m = ( s + e) // 2 
        if target == arr[m]:
            return m
        elif target < arr[m]:
            s = m + 1 
        else:
            e = m - 1 

print(bs_desc(arr, target))
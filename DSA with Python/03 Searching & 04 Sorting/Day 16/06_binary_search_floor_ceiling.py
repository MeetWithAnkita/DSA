# Floor: 
# Greatest element less than or equal to the target.
# Ceiling: 
# Smallest element greater than or equal to the target.

# arr = [3, 6, 9, 12, 15]
# target = 9

arr = [2, 5, 8, 12, 16, 20]
target = 10

def floor_ceiling(arr, target):
    s = 0 
    e = len(arr) - 1 
    while s <= e:
        m = (s + e) // 2 
        if target == arr[m]:
            return arr[m], arr[m]
        elif target < arr[m]:
            e = m - 1 
        else:
            s = m + 1 
    floor = arr[s-1] if s > 0 else None
    ceiling = arr[s] if s < len(arr) else None
    return floor, ceiling
    
floor, ceiling = floor_ceiling(arr, target)
print("Floor: ",floor)
print("Ceiling: ",ceiling)
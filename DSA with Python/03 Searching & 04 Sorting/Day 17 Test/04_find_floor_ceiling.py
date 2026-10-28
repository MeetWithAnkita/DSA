arr = [5, 10, 15, 20, 25, 30]
target = 18

def find_flooe_ceiling(arr, target):
    s = 0 
    e = len(arr) - 1 
    ans = -1

    while s <= e:
        m = (s + e) // 2 
        if target == arr[m]:
            return arr[m], arr[m]
        elif target < arr[m]:
            e = m - 1 
        else:
            s = m + 1 
  
    floor = arr[s - 1] if s >0 else None
    ceil = arr[s ] if s < len(arr) else None
    return (floor, ceil)


print(find_flooe_ceiling(arr, target))
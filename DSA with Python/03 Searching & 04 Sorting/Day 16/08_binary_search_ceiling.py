arr = [2, 5, 8, 12, 16, 20]
target = 10

def ceiing_bs(arr, target):
    s = 0 
    e = len(arr) - 1 
    while s <= e:
        m = ( s + e ) // 2 
        if target == arr[m]:
            return arr[m] 
        elif target < arr[m]:
            e = m - 1 
        else:
            s = m + 1 
    ceiling = arr[s] if s < len(arr) else None 
    return ceiling

print(ceiing_bs(arr, target))


# Time: O(log n)
# Auxiliary Space: O(1)
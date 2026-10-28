arr = [10, 20, 30, 40, 50]
target = 35

def insert_pos(arr, target):
    s = 0 
    e = len(arr) - 1 
    while s <= e:
        m = (s + e) // 2 
        if target == arr[m]:
            return m
        elif target < arr[m]:
            e = m - 1 
        else:
            s = m + 1 
    return s 

print(insert_pos(arr, target))

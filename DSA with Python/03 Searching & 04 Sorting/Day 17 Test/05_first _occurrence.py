arr = [2, 4, 4, 4, 6, 8]
target = 4

def first_occu(arr, target):
    s = 0 
    e = len(arr) - 1 
    ans = -1

    while s <= e:
        m = (s + e) // 2 
        if target == arr[m]:
            ans = m
            e = m - 1 
        elif target < arr[m]:
            e = m - 1 
        else:
            s = m + 1 
    return ans 


print(first_occu(arr, target))

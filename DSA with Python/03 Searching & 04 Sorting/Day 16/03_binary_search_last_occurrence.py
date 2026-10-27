arr = [1, 3, 3, 3, 3, 5, 7]
target = 3

def last_occure(arr, target):
    s = 0 
    e = len(arr) - 1 
    ans = -1
    while s <= e:
        m = (s + e) // 2 
        if arr[m] == target:
            ans = m 
            s = m + 1 
        elif arr[m] > target:
            e = m - 1 
        elif arr[m] < target:
            s = m + 1 
    return ans

print(last_occure(arr, target))
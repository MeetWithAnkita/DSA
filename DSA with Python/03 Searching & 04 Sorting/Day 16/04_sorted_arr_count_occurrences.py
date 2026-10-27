# arr = [1, 3, 3, 3, 3, 5, 7]
# target = 3
# arr = [2, 2, 2, 2, 2, 2]
# target = 2
arr = [2, 4, 6, 8, 10, 12]
target = 7
def count_occurrences(arr, target):
    count = 0 
    s = 0 
    e = len(arr) - 1 
    f_ans = -1
    l_ans = -1
    while s <= e:
        m = (s + e) // 2 
        if arr[m] == target:
            f_ans = m
            e = m - 1 
        elif arr[m] < target:
            s = m + 1 
        elif arr[m] > target:
            e = m - 1 
    
    
    s = 0 
    e = len(arr) - 1 
    while s <= e:
        m = (s + e) // 2 
        if arr[m] == target:
            l_ans = m
            s = m + 1 
        elif arr[m] < target:
            s = m + 1 
        elif arr[m] > target:
            e = m - 1 
            
    print(l_ans)
    print(f_ans)
    if l_ans == -1 and f_ans == -1:
        return 0
    return (l_ans - f_ans + 1)

print(count_occurrences(arr, target))
    
    

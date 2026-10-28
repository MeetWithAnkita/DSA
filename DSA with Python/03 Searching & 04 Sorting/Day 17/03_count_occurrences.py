arr = [1, 2, 2, 2, 2, 3, 4, 5, 5]
target = 2

def count_occurrences(arr, target):
    ans_f = -1
    ans_l = -1

    s = 0 
    e = len(arr) - 1 
    while s <= e:
        m = ( s + e ) // 2 
        if target == arr[m]:
            ans_f = m
            e = m - 1
        elif target < arr[m]:
            e = m - 1 
        else:
            s = m + 1
    
    s = 0 
    e = len(arr) - 1 
    while s <= e:
        m = ( s + e ) // 2 
        if target == arr[m]:
            ans_l = m
            s = m + 1
        elif target < arr[m]:
            e = m - 1 
        else:
            s = m + 1

    return ans_l - ans_f + 1

print(count_occurrences(arr, target))
# arr = [1, 2, 2, 2, 2, 3, 4, 5, 5]
# target = 2
arr = [1, 2]
target = 2


def last_occurrence(arr, target):
    s = 0 
    e = len(arr) - 1 
    ans = -1

    while s <= e:
        m = ( s + e ) // 2 
        if target == arr[m]:
            ans = m 
            s = m + 1 
        elif target < arr[m]:
            e = m - 1 
        else:
            s = m + 1 
    return ans


print(last_occurrence(arr, target))
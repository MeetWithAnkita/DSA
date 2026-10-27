arr = [2, 4, 4, 4, 6, 8, 10]
target = 4 


def first_occurrence_bs(arr, target):
    length = len(arr)
    s = 0 
    e = length -1 
    ans = - 1
    while s <= e:
        m = (s+e) // 2 
        if arr[m] == target:
            ans = m 
            e = m - 1 
            # print(ans)
        elif arr[m] > target:
            # s = m + 1
            e = m - 1  
        elif arr[m] < target:
            s = m + 1 
    return ans

print(first_occurrence_bs(arr, target))

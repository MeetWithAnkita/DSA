# Task:
# Sometimes a question gives you a sorted array 
# but doesn't tell you whether it's ascending or 
# descending.

# Your task is to identify the order first and then 
# perform Binary Search.

arr = [100, 80, 60, 40, 20]
target = 40

def bs(target, arr):
    s = 0 
    e = len(arr) - 1 
    # asc = False 
    # dsc = False 
    # if arr[s] < arr[e]:
    #     asc = True 
    # else:
    #     dsc = True 
    asc = arr[s] < arr[e]
    dsc = arr[s] > arr[e]
    while s <= e:
        m = ( s + e) // 2 
        if target == arr[m]:
            return m
        elif target < arr[m]:
            if asc:
                e = m - 1
            if dsc:
                s = m + 1 
        else:
            if dsc:
                e = m - 1
            if asc:
                s = m + 1 
    return -1
print(bs(target, arr))



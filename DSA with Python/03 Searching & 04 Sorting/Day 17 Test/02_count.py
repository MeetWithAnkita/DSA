# arr = [2, 4, 4, 4, 6, 8]
# target = 4

arr = [1, 2, 2, 2, 2, 3, 4, 5]
target = 2

def count(arr, target):
    ans_f = -1
    ans_l = -1

    s = 0 
    e = len(arr) - 1 
    while s <= e:
        m = (s + e) // 2 
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
        m = (s + e) // 2 
        if target == arr[m]:
            ans_l = m
            s = m + 1 
        elif target < arr[m]:
            e = m - 1 
        else:
            s = m + 1 

    if ans_f == -1 :
        return 0
    else:
        return(ans_f, ans_l)     

first , last = (count(arr, target))

print("First occurrence: ", first)
print("Last occurrence: ", last)
print("Total Count: ", (last - first + 1))
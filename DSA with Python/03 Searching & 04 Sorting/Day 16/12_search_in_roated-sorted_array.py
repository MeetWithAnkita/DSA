# arr = [4, 5, 6, 7, 0, 1, 2]
# target = 0

# arr = [4, 5, 6, 7, 0, 1, 2]
# target = 3

arr = [8, 9, 10, 2, 3, 4, 5, 6]
target = 9 

s = 0 
e = len(arr) - 1 

while s <= e:
    m = ( s+e )// 2 
    if arr[m] == target:
        print(m)
        break
    elif arr[m] >= arr[s]:
        # left half is soted
        if arr[s] <= target < arr[m]:
            e = m - 1
        else:
            s = m + 1 
    elif arr[m] <= arr[e]:
        # right half is sorted
        if arr[m] <= target <= arr[e]:
            s = m + 1  
        else:
            e = m - 1 
else:
    print(-1)
    

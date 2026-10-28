# arr = [4, 5, 6, 7, 8, 0, 1, 2]
# target = 0

arr = [6, 7, 8, 1, 2, 3, 4, 5]
target = 9

def search_bs(arr, target):
    s = 0 
    e = len(arr) - 1 

    while s <= e:
        m = ( s + e ) // 2 
        if target == arr[m]:
            return m
        elif arr[m] >= arr[s]:
            # left hand 
            if arr[s] <= target < arr[m]:
                e = m - 1
            else:
                s = m + 1  
        elif arr[m] < arr[e]:
            # right hand
            if arr[m] <= target <= arr[e]:
                s = m + 1
            else:
                e = m - 1 
    return -1

print(search_bs(arr, target))



# Complexity
# - Time: \(O(\log n)\)
# - Auxiliary Space: \(O(1)\)

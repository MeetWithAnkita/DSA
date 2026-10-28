arr = [2, 4, 4, 4, 6, 8, 10]
target = 4

def find_first_occurrence(arr, target):
    s = 0 
    e = len(arr) - 1 
    ans = -1
    while s <= e:
        m = ( s + e ) // 2 

        if target == arr[m]:
            e = m - 1
            ans = m 
        elif target > arr[m]:
            s = m + 1 
        elif target < arr[m]:
            e = m -1 
    return ans

print(find_first_occurrence(arr, target))


# Complexity: Time O(log n), Auxiliary Space O(1).
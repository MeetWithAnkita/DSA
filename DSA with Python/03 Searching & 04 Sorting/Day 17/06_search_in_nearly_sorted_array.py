# First understand this property:
# In a normal sorted array, 
# an element belongs at its expected sorted position.

# In a nearly sorted array, an element may be at:
# - Its expected position.
# - One position to the LEFT.
# - One position to the RIGHT.

# arr = [10, 3, 40, 20, 50, 80, 70]
# target = 70
arr = [10, 3, 40, 20, 50, 80, 70]
target = 70

def search_in_nearly_sorted_array(arr, target):
    s = 0 
    e = len(arr) - 1 
    while s <= e:
        m = ( s + e ) // 2 
        if target == arr[m]:
            return m 
        elif m > 0 and target == arr[m-1]:
            return (m-1)
        elif m < len(arr)-1 and target == arr[m + 1]:
            return (m+1) 
        elif target < arr[m]:
            e = m - 1 - 1 
        else:
             s = m + 1 + 1
    return - 1



print(search_in_nearly_sorted_array(arr, target))


# Complexity	Value
# Time	O(log n)
# Auxiliary Space	O(1)

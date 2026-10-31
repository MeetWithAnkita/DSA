# Time: O(n)
#  Space: O(1)

# 1. What is the Dutch National Flag Problem?
# Given an array containing only 0, 1, and 2, sort it in ascending order.

# three poninter sorting approach

arr = [2, 0, 1, 2, 1, 0]
#     m/i             h
# [0, 0, 1, 2, 1, 2]
# m/i          h
# [0, 0, 1, 2, 1, 2]
#    m/i       h
# [0, 0, 1, 2, 1, 2]
#       m/i    h
# [0, 0, 1, 2, 1, 2]
#        i  m  h
# [0, 0, 1, 1, 2, 2]
#        i  m/h
def DNF(arr):
    low = 0 
    mid = 0 
    high = len(arr) - 1 

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1 
            mid += 1 
        elif arr[mid] == 1:
            mid += 1 
            # The element coming from the high side has not been examined yet.
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1 
    return arr

print(DNF(arr))


# Metric	        Complexity
# Time	            O(n)
# Auxiliary space	O(1)
# Sorting type	    In-place
# Extra array	    Not required
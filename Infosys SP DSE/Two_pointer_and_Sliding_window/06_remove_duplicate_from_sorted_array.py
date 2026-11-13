# Given a sorted array, remove duplicates in-place so each
#  element appears only once. Return the number of unique 
# elements.

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

def remove_duplicate_from_sorted_array(arr):
    left = 0 
    for i in range(1, len(arr)):
        if arr[left] != arr[i]:
            left += 1
            arr[left] = arr[i]

    return len(arr[:left+1])

print(remove_duplicate_from_sorted_array(nums))

'''
Complexity	|| Result
Time	    || O(n)
Extra space	|| O(1)

Your original function returns a slice, 
which creates a new list and uses O(k) additional space. 
Returning left + 1 avoids that.
'''
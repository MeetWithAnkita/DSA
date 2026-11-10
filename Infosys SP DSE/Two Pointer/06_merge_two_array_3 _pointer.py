nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]

m = 3
n = 3

def merge_using_3_pointer(arr1, arr2, m, n):
    i = m - 1
    j = n - 1 
    k = m + n - 1 

    while i >= 0 and j >= 0:
        if arr1[i] < arr2[j]:
            arr1[k] = arr2[j]
            j -= 1 
        else:
            arr1[k] = arr1[i]
            i -= 1
        k -= 1 
    while j >= 0:
        arr1[k] = arr2[j] 
        j -= 1 
        k -= 1
    return arr1


print(merge_using_3_pointer(nums1, nums2, m, n))


'''
Time complexity: O(m+n).

Extra space complexity: O(1).
'''

'''
Use 3 pointer + in place modification'''

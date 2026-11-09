nums1 = [1, 4, 7, 0, 0, 0]
m = 3

nums2 = [2, 5, 8]
n = 3

def merge(arr1, arr2, m, n):
    i = m - 1 
    j = n - 1 
    k = m + n - 1 
    while i >= 0 and j >= 0 :
        if arr1[i] > arr2[j]:
            arr1[k] = arr1[i] 
            i -= 1
        else:
            arr1[k] = arr2[j] 
            j -= 1
        k -= 1
    while j >= 0:
        arr1[k] = arr2[j]
        j -= 1 
        k -= 1
    return arr1


print(merge(nums1, nums2, m, n))
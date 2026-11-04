nums1 = [1, 2, 2, 3, 4]
nums2 = [3, 4, 5, 6, 6]

def union(arr1, arr2):
    # result = set(arr1) | set(arr2)
    result = set(arr1).union(arr2)
    return result

print(union(nums1, nums2))

# Complexity	Result
# Time	O(n + m) average
# Space	O(n + m)
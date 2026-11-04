'''Given two arrays, return the elements that are present in both arrays, without duplicates.'''
nums1 = [1, 2, 2, 3, 4, 5]
nums2 = [2, 2, 3, 6, 7]

def intersection(arr1, arr2):
    # intersection = set()
    # for i in arr1:
    #     if i in intersection:
    #         continue
    #     else:
    #         if i in arr2:
    #             intersection.add(i)

    seen = set()
    result = set()

    for num in arr1:
        if num in arr2:
            result.add(num)
    return result
    # return intersection


print(intersection(nums1, nums2))
'''
LeetCode 34 
Find First and Last Position of Element in Sorted Array.
'''
nums = [5, 7, 7, 8, 8, 8, 10]
target = 8

# Expected output: [3, 4]

def first_occurrence(nums, target):
    left = 0 
    right = len(nums) - 1 
    f_ans = -1
    l_ans = -1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            f_ans = mid
            right = mid - 1 
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
         
    return f_ans
# print(first_occurrence(nums, target))

def last_occurrence(nums, target):
    left = 0 
    right = len(nums) - 1 
    ans = -1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            ans = mid
            left = mid + 1 
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
         
    return ans
# print(last_occurrence(nums, target))


def search_range(nums, target):
    first = first_occurrence(nums, target)
    last = last_occurrence(nums, target)

    return [first, last]

print(search_range(nums, target))

'''
Time Complexity:
O(log n)+O(log n)=O(log n)
'''
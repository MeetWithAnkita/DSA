'''
Problem: Given a sorted array of distinct integers and a 
target, return the index if the target exists. Otherwise, 
return the index where it should be inserted to maintain 
sorted order.
'''
nums = [1, 3, 5, 6]
target = 2

# Expected output: 1
def serach_insert_pos(nums, target):
    left = 0 
    right = len(nums) - 1 
    while left <= right:
        mid = (left + right) // 2 
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            left = mid + 1 
        else:
            right = mid - 1
    return left 


print(serach_insert_pos(nums, target))

'''
Complexity
- Time: O(log n)
- Auxiliary space: O(1)
'''
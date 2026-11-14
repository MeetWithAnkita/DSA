nums = [-1, 0, 3, 5, 9, 12]
target = 9

# Expected output: 4

def binary_search(nums, target):
    left = 0 
    right = len(nums) - 1 
    while left <= right:
        mid = (left + right) // 2 
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            left = mid+1
        else:
            right = mid - 1
    return -1

print(binary_search(nums, target))
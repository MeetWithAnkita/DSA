nums = [3, 4, 5, 1, 2]
# Expected output: 1

def find_min(nums):
    left = 0 
    right = len(nums) - 1
    min_value = float('inf')
    while left < right:
        mid = left + (right - left) // 2 
        min_value = min(min_value, nums[mid])
        if nums[mid] >= nums[right]:
            left = mid + 1 
            
        elif nums[mid] <= nums[right]:
            right = mid 
            # mid might eventually point to the minimum. 
            # Therefore, we preserve it using

    return min_value
print(find_min(nums))

'''
Complexity	Your solution
Time	        O(log n)
Space	        O(1)
'''
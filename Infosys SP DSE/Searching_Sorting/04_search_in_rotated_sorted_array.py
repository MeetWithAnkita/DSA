nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

# Expected output: 4

def search(nums, target):
    left = 0 
    right = len(nums) - 1 
    while left <= right:
        mid = (left + right) // 2 
        if nums[mid] == target:
            return mid 
        else:
            if nums[left] <= nums[mid]:
                # left side sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1 
                else:
                    left = mid + 1 
            elif nums[mid] <= mid[right]:
                # right side sorted 
                if nums[mid] < target <= nums[right]:
                    left = mid + 1 
                else:
                    right = mid - 1 
            
    return -1

print(search(nums, target))

'''
Complexity	        Value
-------------------------------
Best time	        O(1)
Average time	    O(log n)
Worst time	        O(log n)
Auxiliary space	    O(1)
'''
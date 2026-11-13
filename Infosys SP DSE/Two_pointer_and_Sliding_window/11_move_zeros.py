'''
Move Zeroes

Given an integer array, move all zeroes to the end while maintaining the relative order of non-zero elements.
'''
nums = [0, 1, 0, 3, 12]

# Expected:
# [1, 3, 12, 0, 0]

def move_zeros(nums):
    left = 0 
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[left] = nums[left], nums[i]
            left += 1
    return nums

print(move_zeros(nums))
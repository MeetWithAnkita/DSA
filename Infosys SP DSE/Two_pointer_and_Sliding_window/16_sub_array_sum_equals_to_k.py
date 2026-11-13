'''
Subarray Sum Equals K (LeetCode 560)

Given an integer array nums and an integer k, return the 
total number of continuous subarrays whose sum equals k.
'''
nums = [1, 1, 1]
k = 2

# Expected output: 2
def no_of_sub_array(nums, k):
    freq = {0 : 1}
    count = 0 
    total = 0
    for i in range(len(nums)):
        total += nums[i]
        
        need = total - k
        count += freq.get(need, 0)
        freq[total] = freq.get(total, 0) + 1
    return count
        
print(no_of_sub_array(nums, k))
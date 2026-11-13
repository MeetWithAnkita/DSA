'''
Longest Subarray With Sum At Most K

Given an array of non-negative integers and an integer k, 
find the length of the longest contiguous subarray whose 
sum is at most k.
'''
nums = [1, 2, 1, 0, 1, 1, 0]
k = 4

# Expected output: 5

def longest_sub_array(nums, k):
    left = 0 
    max_len = float('-inf')
    window_sum = 0 

    for r in range(len(nums)):
        v = nums[r]
        window_sum += v

        while window_sum > k:
            window_sum -= nums[left]
            left += 1
        cur_length = (r - left + 1)
        max_len = max(max_len, cur_length)
    return max_len
print(longest_sub_array(nums, k))

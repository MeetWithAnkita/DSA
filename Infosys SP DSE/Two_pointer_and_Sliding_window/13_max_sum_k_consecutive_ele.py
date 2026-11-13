'''
Given an array of integers and a number k, 
find the maximum sum of any k consecutive elements.
'''
nums = [2, 1, 5, 1, 3, 2]
k = 3

# Expected output: 9

def max_sum(nums, k):
    total = sum(nums[:k])
    max_t = total 

    for i in range(k, len(nums)):
        total += nums[i]
        total -= nums[i - k]

        max_t = max(max_t, total)
    return max_t

print(max_sum(nums, k))
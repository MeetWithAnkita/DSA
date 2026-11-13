'''
Maximum Sum of a Subarray of Size K

Given an array of positive integers and an integer k, 
find the maximum sum of any contiguous subarray of size k.
'''

nums = [2, 1, 5, 1, 3, 2]
k = 3

# Expected output: 9

def max_sum_sub_array(arr, k):
    total = sum(arr[:k])
    max_total = total 
    for i in range(k, len(arr)):
        total += arr[i]
        total -= arr[i - k]
        max_total = max(max_total, total)
    return max_total

print(max_sum_sub_array(nums, k))
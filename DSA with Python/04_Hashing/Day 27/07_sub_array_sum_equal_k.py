'''
Task: Return the total number of continuous subarrays 
whose sum equals k.
'''

nums = [3, 4, -7, 1, 3, 3, 1, -4]
k = 7

def no_of_sub_array(nums, k):
    freq = {0:1}
    count = 0 
    prefix_sum = 0

    for i in nums:
        prefix_sum += i 
        need = prefix_sum - k 
        count += freq.get(need, 0)
        freq[prefix_sum] = freq.get(prefix_sum, 0) + 1
    return count

print(no_of_sub_array(nums, k))
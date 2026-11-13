'''
Given an integer array nums and an integer k, return the 
total number of continuous subarrays whose sum equals k.
'''
'''
Use: Prefix Sum + Hashing
'''
# nums = [1, 2, 3]
# k = 3

nums = [1, -1, 1]
k = 1

def sub_array_sum_k(arr, k):
    freq = {0: 1}
    count = 0 
    current_total = 0 
    for i in range(len(arr)):
        current_total += arr[i]
        need = current_total - k
        count += freq.get(need, 0)
        freq[current_total] = freq.get(current_total, 0) + 1 
    return count
    
print(sub_array_sum_k(nums, k))

'''
Complexity:
- Time: O(n) average
- Space: O(n)
'''
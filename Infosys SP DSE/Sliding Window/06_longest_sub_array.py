'''
Find the longest contiguous subarray whose sum is at most 
K.
'''

arr = [1, 2, 1, 0, 1, 1, 0]
k = 4

def sub_array_most_sum(arr, k):
    left = 0 
    max_length = 0 
    max_total = 0 
    for right in range(len(arr)):
        max_total += arr[right]
        while max_total > k:
            max_total -= arr[left]
            left += 1 
        current_length = right - left + 1 
        max_length = max(max_length, current_length)
    return max_length


print(sub_array_most_sum(arr, k))
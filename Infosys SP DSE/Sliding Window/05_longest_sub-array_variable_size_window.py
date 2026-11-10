'''
Longest Subarray with Sum at Most K

Find the length of the longest contiguous subarray whose 
sum is at most K.
'''

arr = [2, 3, 1, 2, 4, 3]
k = 5

def max_len(arr, k):
    left = 0 
    window_sum = 0 
    max_length = 0 
    for right in range(len(arr)):
        window_sum += arr[right] 
        while window_sum > k:
            window_sum -= arr[left]
            left += 1 
        current_length = right - left + 1 
        max_length = max(max_length, current_length)
    return max_length

print(max_len(arr, k))
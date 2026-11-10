'''
Find the shortest subarray whose sum is at least K.
'''
arr = [2, 3, 1, 2, 4, 3]
k = 7

def shorest_sub_array(arr, k):
    left = 0 
    total = 0 
    min_len = float('inf')

    for r in range(len(arr)):
        total += arr[r]
        while total >= k:
            current_len = r - left +1
            min_len = min(min_len, current_len)

            total -= arr[left]
            left += 1 
    if min_len == float('inf'):
        return 0
    return min_len
    
print(shorest_sub_array(arr, k))

'''
Complexity: O(n) time and O(1) extra space.
'''
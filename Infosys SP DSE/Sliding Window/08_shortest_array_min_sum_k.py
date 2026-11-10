arr = [1, 2, 3, 4, 5]
k = 11

def short_sub_array(arr, k):
    left = 0 
    min_len = float('inf')
    total = 0
    for r in range(len(arr)):
        total += arr[r]

        while total >= k:
            current_len = r - left + 1 
            min_len = min(min_len, current_len)
            total -= arr[left]
            left += 1
    if min_len == float('inf'):
        return 0
    return min_len

print(short_sub_array(arr, k))
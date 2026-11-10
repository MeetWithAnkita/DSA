'''
Find the maximum sum of any 3 consecutive elements.
'''

arr = [2, 1, 5, 1, 3, 2]
k = 3 

def max_sum_k_window(arr, k):
    total = sum(arr[:k])
    max_total = total 
    for i in range(k, len(arr)):
        total = total - arr[i-k] + arr[i]
        # if total > max_total:
        #     max_total = total 
        max_total = max(max_total, total)
    return max_total

print(max_sum_k_window(arr, k))

'''
This is exactly the standard fixed-size Sliding Window 
pattern.
time: O(n)
'''
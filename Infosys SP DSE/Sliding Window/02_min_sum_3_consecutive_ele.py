# arr = [4, 2, 7, 1, 8, 3]
# k = 3
arr = [-5, -2, -8, -1, -3]
k = 2
# -15
# -11
# -12

def min_total_k_consecutive_ele(arr, k):
    total = sum(arr[:k])
    min_total = total
    for i in range(k, len(arr)):
        total = total - arr[i-k] + arr[i]
        min_total = min(min_total, total)
    return min_total 

print(min_total_k_consecutive_ele(arr, k))

'''
Complexity
- Time:         O(n)
- Extra space:  O(1)
'''

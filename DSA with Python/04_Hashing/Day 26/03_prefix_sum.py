arr = [3, 2, 5, 1, 6, 4]
L = 1
R = 4
def range_sum(prefix, L, R):
    if L == 0:
        result = prefix[R] 
        return result
    else:
        result = prefix[R] - prefix[L-1]
        return result


def prefix_sum(arr):
    prefix = [0] * len(arr)

    # Your code here
    prefix[0] = arr[0]
    for i in range(1, len(arr)):
        prefix[i] = prefix[i-1] + arr[i]
    return prefix

prefix = prefix_sum(arr)

print(range_sum(prefix, L, R))
print(range_sum(prefix, 2, 5))  # 16
print(range_sum(prefix, 0, 3))  # 11

'''
Time: O(n) — one traversal.
Space: O(n) — the prefix array.
'''


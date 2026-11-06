nums = [4, 2, 7, 1, 3, 5]

queries = [
    (1, 3),
    (0, 4),
    (2, 5)
]
def prefix_sum(nums):
    prefix_sum = [0] * (len(nums))
    prefix_sum[0] = nums[0]
    for i in range(1, len(nums)):
        prefix_sum[i] = prefix_sum[i-1] + nums[i]
    return prefix_sum

def sum_range(prefix_sum, L, R):
    if L == 0:
        return prefix_sum[R]
    else:
        return  prefix_sum[R] - prefix_sum[L - 1]

prefix_sum = prefix_sum(nums)
for i in queries:
    L,R = i 
    print(sum_range(prefix_sum, L, R))

'''
Building prefix sum: O(n). 
Each query: O(1). 
Total: O(n + q).
'''

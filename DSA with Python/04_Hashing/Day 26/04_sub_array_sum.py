nums = [1, 2, 3]
k = 3
def subarray_sum(nums, k):
    freq = {0: 1}
    current_sum = 0
    count = 0

    for num in nums:
        current_sum += num # 0+ 1 = 1

        # 1. Calculate the prefix sum we need to find
        need = current_sum - k # 1 - 3 = -2

        # 2. Update count using freq
        count += freq.get(need, 0) #count = 0 + 0 = 0 

        # 3. Store the current prefix sum
        freq[current_sum] = freq.get(current_sum, 0) + 1
        # freq[1] = 1 


    return count

print(subarray_sum(nums, k))  # Expected: 2
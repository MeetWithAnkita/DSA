nums = [1, 2, 1, 2, 1]
k = 3

def sub_array_sum_equal_k(nums, k):
    count = 0 
    current_sum = 0
    freq= {0:1}
    for i in nums:
        current_sum += i 
        need = current_sum - k 
        count += freq.get(need, 0)
        freq[current_sum] = freq.get(current_sum, 0) + 1 
    return count

print(sub_array_sum_equal_k(nums, k))
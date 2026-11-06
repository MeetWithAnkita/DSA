# prefix sum + hashing technique.


nums = [1, -1, 0]
k = 0

def count_sub_array_sum(nums, k):
    current_sum = 0
    freq = {0:1}
    count = 0 
    for i in nums:
        current_sum += i 
        need = current_sum - k
        count += freq.get(need, 0)
        freq[current_sum] = freq.get(current_sum, 0) + 1 
    return count


print(count_sub_array_sum(nums, k))
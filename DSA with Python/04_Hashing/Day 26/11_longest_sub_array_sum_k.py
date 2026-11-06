nums = [2, 0, 0, 3, 2, 1, 1, 1]
k = 6

def find_longest_sub_array(nums, k):
    freq = {0 : -1}
    count = 0 
    current_sum = 0 
    max_len = 0 

    for i in range(len(nums)):
        current_sum += nums[i]
        need = current_sum - k 
        if need in freq:
            count = i - freq[need]
            max_len = max(max_len, count)
        if current_sum not in freq:
            freq[current_sum] = i
    return max_len

print(find_longest_sub_array(nums, k))
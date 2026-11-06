nums = [10, 5, 2, 7, 1, 9]
k = 15

def longest_sub_array(nums, k):
    prefix_sum = 0 
    max_length = 0
    first_index = {0: -1}

    for i in range(len(nums)):
        prefix_sum += nums[i]
        need = prefix_sum - k 
        if need in first_index:
            length = i - first_index[need]
            max_length = max(length, max_length)
        if prefix_sum not in first_index:
            first_index[prefix_sum] = i

    return max_length      
        
print(longest_sub_array(nums, k))
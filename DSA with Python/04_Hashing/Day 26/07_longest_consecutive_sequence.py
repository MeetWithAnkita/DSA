nums = [100, 4, 200, 1, 3, 2]

def find_longest_consecutive_sequence(nums):
    length = 0 
    max_len = 0 

    num_set = set(nums)
    for i in num_set:
        if i-1 not in num_set:
            current = i 
            count = 1 
            while current+1 in num_set:
                count += 1 
                current += 1 
            max_len = max(max_len, count)
    return max_len

print(find_longest_consecutive_sequence(nums))
nums = [9, 1, 4, 7, 3, 2, 6, 8, 100, 5]

def find_longest_sequence(nums):
    num_set = set(nums)
    max_length = 0 
    for i in num_set:
        if i-1 not in num_set:
            current = i 
            count = 1 
            while current+1 in num_set:
                current += 1 
                count += 1 
            max_length = max(max_length, count)
    return max_length

print(find_longest_sequence(nums))
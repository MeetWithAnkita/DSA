nums = [4, 5, 1, 2, 1, 4, 5, 3]

def first_non_repeat_ele(nums):
    freq = {}
    for i in nums:
        freq[i] = freq.get(i, 0) + 1 
    for i in nums:
        if freq[i] == 1:
            return i

print(first_non_repeat_ele(nums))
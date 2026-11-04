nums = [10, 5, 3, 4, 3, 5, 6]

def repeating_ele(nums):
    freq = {}
    for i in nums:
        freq[i] = freq.get(i, 0) + 1 
    for i in nums:
        if freq[i] > 1:
            return i
print(repeating_ele(nums))
nums = [1, 1, 1, 2, 2, 3]
k = 2

def find_top_k_ele(nums, k):
    freq = {}
    for i in nums:
        freq[i] = freq.get(i, 0) + 1 
    l = []
    while len(l) < k:
        max_ele = None
        max_freq = 0 
        for i in freq:
            if freq[i] > max_freq:
                max_freq = freq[i]
                max_ele = i 
        l.append(max_ele)
        del freq[max_ele]
    return l

print(find_top_k_ele(nums, k))

'''
Operation	Complexity
Frequency counting	O(n)
Finding maximum frequency	O(m)
Repeating maximum search k times	O(k * m)
Total time	O(n + k * m)
Space	O(m)
'''
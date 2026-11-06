'''
Given an integer array nums and an integer k, return the 
k most frequent elements. You may return the answer in any 
order.
'''

nums = [1,1,1,2,2,3]
k = 2

freq = {}
for i in nums:
    freq[i] = freq.get(i, 0) + 1 
print(freq)

l = []

while len(l) < k:
    max_freq = 0
    max_ele = 0
    for i in freq:
        if freq[i] > max_freq:
            max_freq = freq[i]
            max_ele = i
    l.append(max_ele)
    del freq[max_ele]

print(l)
    
    



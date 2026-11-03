arr = [1, 2, 2, 3, 1, 2, 4]

freq = {}
for i in arr:
    if i not in freq:
        freq[i] = 1
    else:
        freq[i] += 1
print(freq)

freq1 = {}
for i in arr:
    freq1[i] = freq1.get(i, 0) + 1
print(freq1)



'''Complexity	Value
Time	        O(n) average
Space	        O(k)

Where:
- n = Number of array elements.
- k = Number of distinct elements.'''
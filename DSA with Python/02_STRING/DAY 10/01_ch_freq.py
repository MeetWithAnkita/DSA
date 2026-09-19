s = "banana"

freq = {}
for i in s: 
    freq[i] = freq.get(i, 0) + 1 
print(freq)


# Complexity
# Time: O(n)
# Space: O(k), where k = number of unique characters
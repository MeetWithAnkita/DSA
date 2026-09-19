s = "AaBbAacc"

freq = {}
for i in s:
    freq[i] = freq.get(i, 0)+ 1
print(freq)

# Complexity

# Time: O(n)
# Space: O(k), where k = unique characters.
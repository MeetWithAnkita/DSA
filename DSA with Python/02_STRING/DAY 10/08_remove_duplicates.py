s = "programming"

# Create a new string containing each character only once, while preserving its original order.
# Expected: progamin
res = ""
freq = {}
for  i in s:
    if i not in freq:
        freq[i] = 1 
        res += i

print(res)


# Your dictionary approach:

# Time: O(n) average for membership
# Space: O(k)

# The set approach has the same average complexity.
# Anagram:
# Two strings are anagrams if they contain the same characters with 
# the same frequencies, regardless of order.

s1 = "listen"
s2 = "silent"

freq = {}
freq2 = {}
for i in s1:
    freq[i] = freq.get(i, 0) + 1 
for i in s2:
    freq2[i] = freq2.get(i, 0) + 1 
if freq == freq2:
    print("Anagram")
else:
    print("Not Anagram")

# ⏱️ Complexity

# Let n and m be the lengths of the two strings.

# Build freq → O(n)
# Build freq2 → O(m)
# Compare dictionaries → O(k), where k = distinct characters

# Overall:

# Time: O(n + m)
# Space: O(k)

# For equal-length strings, we generally write:

# Time: O(n)
# Space: O(k)

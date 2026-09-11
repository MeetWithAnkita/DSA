# Hashing 
arr = [4, 1, 2, 4, 3, 1, 4, 2]
freq = {}
for i in arr:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1 
print(freq)

# Complexity
# Time: O(n) average
# Extra Space: O(n) in the worst case
# Pattern: Hashing / Frequency Counting
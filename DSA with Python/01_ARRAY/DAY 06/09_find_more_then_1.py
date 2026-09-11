arr = [4, 2, 7, 4, 2, 9, 2, 7, 5]
freq = {}
for i in arr:
    if i in freq:
        freq[i] += 1 
    else:
        freq[i] = 1
for i in freq:
    if freq[i] > 1:
        print(i, "->", freq[i])
# Complexity
# Building frequency: O(n) average
# Finding duplicates: O(n)
# Total: O(n) average
# Extra space: O(n)
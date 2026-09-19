s = "python is easy python is powerful python"

s_l = s.split()
freq = {}
for i in s_l:
    freq[i] = freq.get(i, 0) + 1 

max_freq = 0
for i in freq:
    if max_freq < freq[i]:
        max_freq = freq[i]

print("Most frequent word: ", end = "")
for i in freq:
    if freq[i] == max_freq:
        print(i)

# Complexity
# Let n = number of words and k = number of unique words.
# Time: O(n)
# Space: O(k)

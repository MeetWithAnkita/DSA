# Find and print all words that appear more than once, along with their frequency.
s = "python is easy python is powerful python is easy"
freq = {}
l_s = s.split()
for i in l_s:
    freq[i] = freq.get(i, 0) + 1 
for i in freq:
    if freq[i] > 1:
        print(i, " -> ", freq[i])
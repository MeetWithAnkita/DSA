s = "programming"

freq = {}
for i in s:
    freq[i] = freq.get(i, 0) + 1
min_freq = float('inf')
for i in freq:
    if min_freq > freq[i]:
        min_freq = freq[i]
for i in freq:
    if min_freq == freq[i]:
        print(i)
s = "aabbccdde"
freq = {}
for i in s:
    freq[i] = freq.get(i, 0) + 1 
for i in freq:
    if freq[i] == 2:
        print(i)
        break
s = "programming"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1 
for i in s:
    if freq[i] == 1:
        print(i)
        break
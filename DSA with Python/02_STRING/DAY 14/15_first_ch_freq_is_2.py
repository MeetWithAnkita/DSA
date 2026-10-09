# Find the first character whose frequency is exactly 2.
s = "aabbccdde"

freq = {}
for i in s:
    freq[i] = freq.get(i, 0) + 1 
    if freq[i] == 2:
        print(i)
        break
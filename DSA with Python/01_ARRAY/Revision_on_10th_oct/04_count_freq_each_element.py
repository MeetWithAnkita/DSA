arr = [2, 3, 2, 5, 3, 2]

freq = {}
for i in arr:
    freq[i] = freq.get(i, 0) + 1 
print(freq)
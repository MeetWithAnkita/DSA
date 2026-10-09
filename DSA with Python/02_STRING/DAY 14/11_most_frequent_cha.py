s = "programming"
freq = {}
for i in s:
    freq[i] = freq.get(i, 0) + 1 
max_freq = 0
var = ""
for i in freq:
    if freq[i] > max_freq:
        max_freq = freq[i]
        var = i
print(var)

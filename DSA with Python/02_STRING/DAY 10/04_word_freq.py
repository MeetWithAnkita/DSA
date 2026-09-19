s = "python is easy python is powerful"

s = s.split()
freq = {}
for i in s :
    freq[i] = freq.get(i, 0 ) + 1
print(freq)

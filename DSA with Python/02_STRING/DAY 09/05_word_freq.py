s = "python java python c java python"

w = s.split()
freq = {}
for i in w:
    if i in freq:
        freq[i] += 1 
    else:
        freq[i] = 1
print(freq)

freq1 = {}
for word in w:
    freq1[word] = freq1.get(word, 0) + 1  
print(freq1)
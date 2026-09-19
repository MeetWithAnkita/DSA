# s = "aabbcde"
s = "swiss"
freq = {}
for i in s:
    freq[i] = freq.get(i, 0) + 1 
for i in s:
    if freq[i] == 1 :
        print("First non-repeating ch: ",i)
        break
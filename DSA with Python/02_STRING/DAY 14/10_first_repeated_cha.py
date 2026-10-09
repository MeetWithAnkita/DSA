s = "abcdefca"

freq = {}
for i in s:
    freq[i] = freq.get(i, 0) + 1 
    if freq[i] > 1:
        print(i)
        break


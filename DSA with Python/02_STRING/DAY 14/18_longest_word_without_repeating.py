s = "apple banana orange"
s_list = list(s.split())
store = []
for i in s_list:
    freq = {}
    for j in i:
        freq[j] = freq.get(j, 0) + 1 
    if len(freq) == len(i):
        store.append(i)
    freq = {}
print(" ".join(store))


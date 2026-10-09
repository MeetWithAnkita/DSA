# s = "aabbccddeeff"
# s = "aabbcccdddde"
s = "aabbcccccddd"
freq = {}
for i in s:
    freq[i] = freq.get(i, 0) + 1 
print(freq)
l = 0
sl = 0
l_var = ""
sl_var = ""
for i in freq:
    if freq[i] > l and freq[i] >sl:
        sl = l
        l = freq[i]
        sl_var = l_var
        l_var = i
    elif freq[i] <l and freq[i] >sl:
        sl = freq[i]
        sl_var = i
print(sl_var)

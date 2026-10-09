s = "aabbcccdddde"
# Find the character with the second-highest frequency.
freq = {}

for i in s:
    freq[i] = freq.get(i, 0 ) + 1
l_f = 0
s_f = 0 
l_str = ""
s_str = ""
for i in freq:
    if l_f < freq[i] and s_f < freq[i]:
        s_f = l_f
        l_f = freq[i]
        s_str = l_str 
        l_str = i
    elif l_f > freq[i] and s_f < freq[i]:
        s_str = i
        s_f = freq[i]

print(s_str)
    
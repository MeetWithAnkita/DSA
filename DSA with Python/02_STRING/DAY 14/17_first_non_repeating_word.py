# Task:
# Find the first word that appears exactly once, preserving the original word order.

s = "apple banana apple mango banana orange"
s_list = list(s.split())
print(s_list)
freq = {}
for i in s_list:
    freq[i] = freq.get(i, 0) + 1 
for i in s_list:
    if freq[i] == 1:
        print(i)
        break



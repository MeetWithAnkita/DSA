'''
Given a string array words, return an array of all characters that show up in 
all strings within the words (including duplicates). You may return the answer 
in any order.

Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]
'''
words = ["bella","label","roller"]

freq1 = {}
freq2 = {}
freq3 = {}

for i in words[0]:
    freq1[i] = freq1.get(i, 0) + 1 
for i in words[1]:
    freq2[i] = freq2.get(i, 0) + 1 
for i in words[2]:
    freq3[i] = freq3.get(i, 0) + 1 

print(freq1)
print(freq2)
print(freq3)
c_f = {}
for k in freq1:
    if k in freq2:
        min_f = min(freq1[k], freq2[k])
    else:
        min_f = 0 
    c_f[k] = min_f
print(c_f)

c_ff = {}
for k in c_f:
    if k in freq3:
        min_ff = min(freq3[k], c_f[k])
    else:
        min_ff = 0 
    c_ff[k] = min_ff
print(c_ff)

l = []
for i in c_ff:
    if c_ff[i] != 0:
        for j in range(c_ff[i]):
            l.append(i)
print(l)



    

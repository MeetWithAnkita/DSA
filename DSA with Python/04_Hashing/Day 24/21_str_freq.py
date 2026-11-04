'''
Given a string s, sort it in decreasing order based on the frequency of 
the characters. The frequency of a character is the number
of times it appears in the string.
'''

s = "tree"
freq = {}
for i in s:
    freq[i] = freq.get(i, 0 ) + 1

sorted_freq = sorted(freq.items(), key = lambda x: x[1], reverse = True)
print(sorted_freq)

l = []
for e,v in sorted_freq:
    l.append(e * v)
print(''.join(l))


'''
Repeatedly find the maximum frequency — O(n + k²).
Sort dictionary items by frequency — O(n + k log k).
'''
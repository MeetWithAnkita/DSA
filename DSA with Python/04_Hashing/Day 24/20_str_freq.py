'''
Given a string s, sort it in decreasing order based on the frequency of 
the characters. The frequency of a character is the number
of times it appears in the string.
'''

s = "tree"
freq = {}
for i in s:
    freq[i] = freq.get(i, 0 ) + 1
# print(freq)

l = []
while len(freq) > 0:
    max_freq = 0

    for e,v in freq.items():
        if v > max_freq:
            max_freq = v
            m_i = e

    # print(max_freq)
    # print(m_i)
    for i in range(int(max_freq)):
        l.append(m_i)   
        freq[m_i] -= 1

    del freq[m_i]  
    # print(freq)

print(''.join(l))

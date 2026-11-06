'''
Task: 
Given a string, sort its characters in descending order 
based on frequency.
'''

s = "tree"

def sort_in_desc(s):
    freq = {}
    for i in s:
        freq[i] = freq.get(i, 0) + 1 
    l = []
    while freq:
        max_ele = None 
        max_freq = 0
        for i in freq:
            if freq[i] > max_freq:
                max_freq = freq[i]
                max_ele = i 
        l.append(str(max_ele) * int(max_freq))
        del freq[max_ele]
    return ("".join(l))

print(sort_in_desc(s))
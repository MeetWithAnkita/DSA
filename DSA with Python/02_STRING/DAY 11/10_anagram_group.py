strs = ["eat","tea","tan","ate","nat","bat"]

groups = {}

for word in strs:
    k = ''.join(sorted(word))

    if k in groups:
        groups[k].append(word)
    else:
        groups[k] = [word]

print(list(groups.values()))


'''
Complexity	Value
==========================
Time	    O(n × k log k)
Space	    O(n × k)
'''




'''
You are given two strings, s1 and s2.

Return True if s2 contains a permutation of s1. Otherwise, 
return False.

A permutation means rearranging the same characters in a 
different order.
'''

# s1 = "ab"
# s2 = "eidbaooo"

s1 = "abc"
s2 = "eidbacoo"

def permutation_in_string(s1, s2):
    if len(s1) > len(s2):
        return False
    
    freq = {}
    for i in s1:
        freq[i] = freq.get(i, 0) + 1 

    window_size = len(s1)
    cu_freq = {}

    for i in range(window_size):
        cu_freq[s2[i]] = cu_freq.get(s2[i], 0) + 1 
    if cu_freq == freq:
        return True 
    else:
        for i in range(window_size, len(s2) ):
            cu_freq[s2[i]] = cu_freq.get(s2[i], 0) + 1 
            cu_freq[s2[i - window_size]] -= 1
            if cu_freq[s2[i - window_size]] == 0 :
                del cu_freq[s2[i - window_size]]
            if cu_freq == freq:
                return True 
        return False 
    
print(permutation_in_string(s1, s2))

'''
Complexity
Let n = len(s2) and m = len(s1).
- Time: O(n + m) with a fixed 26-character alphabet.
- Auxiliary space: O(1) with a fixed alphabet.
'''
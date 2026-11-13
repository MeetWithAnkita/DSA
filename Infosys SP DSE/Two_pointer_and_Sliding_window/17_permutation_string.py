'''
Given two strings s1 and s2, return True if s2 contains a 
permutation of s1. Otherwise, return False.
'''

s1 = "ab"
s2 = "eidbaooo"

# Expected output: True
def check_valid(s1, s2):
    if len(s1) > len(s2):
        return False 
    
    freq = {}
    for i in s1:
        freq[i] = freq.get(i, 0) + 1 

    k = len(s1) #window size 
    check = {}

    for i in range(k):
        ch = s2[i]
        check[ch] = check.get(ch, 0) + 1 

    left = 0
    for i in range(k, len(s2)):
        if check == freq:
            return True
        else:
            ch = s2[i]
            check[s2[left]] -= 1
            if check[s2[left]] == 0:
                del check[s2[left]]
            left += 1
            check[ch] = check.get(ch, 0) + 1 
    return False          

print(check_valid(s1, s2))
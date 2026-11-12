'''
You are given two strings, s and t.

Find the minimum-length substring of s that contains all 
characters of t, including their required frequencies.

If no such substring exists, return an empty string "".
'''

s = "ABBCAC"
t = "ABC"

def min_sub_string(s, t):
    if len(s) < len(t):
        return ""
    need = {}
    for i in t:
        need[i] = need.get(i, 0) + 1 

    left = 0 
    start = 0 
    freq = {}
    min_len = float('inf')
    have = 0 
    required = len(need)

    for i in range(len(s)):
        ch = s[i]
        freq[ch] = freq.get(ch, 0) + 1 
        if ch in need and freq[ch] == need[ch]:
            have += 1 

        while have == required:
            curr_len = (i - left + 1)
            min_len = min(min_len, curr_len)

            start = left 
            freq[s[left]] -= 1

            if freq[s[left]] in need and freq[s[left]] < need[s[left]]:
                have -= 1
            if freq[s[left]] == 0:
                del freq[s[left]] 

            left += 1 
            
    if min_len == float('inf'):
        return ""
    else:
        return (s[start : start+min_len])
    
print(min_sub_string(s, t))
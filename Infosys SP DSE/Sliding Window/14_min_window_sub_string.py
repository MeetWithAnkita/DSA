'''
You are given two strings, s and t.

Find the minimum-length substring of s that contains all 
characters of t, including their required frequencies.

If no such substring exists, return an empty string "".
'''

s = "ADOBECODEBANC"
t = "ABC"

def min_len_sub_string(s, t):
    if len(s) < len(t):
        return ""
    need = {}
    for i in t:
        need[i] = need.get(i, 0) + 1

    left = 0 
    have = 0 
    required = len(need) 
    window = {}

    min_len = float('inf')
    start = 0 

    for i in range(len(s)):
        # expand ..
        ch = s[i]
        window[ch] = window.get(ch, 0) + 1 
        if ch in need and window[ch] == need[ch]:
            have += 1

        # shink while valid
        while required == have:
            min_len = min(min_len, (i - left + 1))
            start = left

            window[s[left]] -= 1

            if s[left] in need and window[s[left]] < need[s[left]]:
                have -= 1
            if window[s[left]] == 0:
                del window[s[left]]

            left += 1
    if min_len == float('inf'):
        return ""
    else:
        return s[start : start+min_len]

print(min_len_sub_string(s, t))
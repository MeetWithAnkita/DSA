'''
Given a string s, find the length of the longest substring without repeating characters.
'''

s = "abcabcbb"

def sub_string_no_repeat(s):
    left = 0
    freq = {}
    max_len = float('-inf')
    for i in range(len(s)):
        ch = s[i]
        freq[ch] = freq.get(ch,0) + 1 

        while freq[ch] > 1:
            freq[s[left]] -= 1 
            if freq[s[left]] == 0:
                del freq[s[left]]
            left += 1 
        curr_len = (i - left + 1 )
        max_len = max(max_len, curr_len)

    return max_len

print(sub_string_no_repeat(s))

'''
Complexity	Value
Time	    O(n)
Space	    O(min(n, character set size))
'''
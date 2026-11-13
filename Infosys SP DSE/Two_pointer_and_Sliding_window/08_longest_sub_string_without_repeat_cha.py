'''
Longest Substring Without Repeating Characters 
(LeetCode 3)

Given a string s, find the length of the longest substring 
without repeating characters.
'''

s = "abcabcbb"

# Expected output: 3
def longest_sub_string_no_repeat(s):
    left = 0 
    max_len = float('-inf')
    freq = {}

    for i in range(len(s)):
        ch = s[i]
        freq[ch] = freq.get(ch, 0) + 1 
        while freq[ch] > 1:
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                del freq[s[left]]
            left += 1 
        curr_len = (i - left + 1 )
        max_len = max(max_len, curr_len)
    return max_len

print(longest_sub_string_no_repeat(s))
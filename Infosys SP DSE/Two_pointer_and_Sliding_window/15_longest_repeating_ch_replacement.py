'''
Longest Repeating Character Replacement (LeetCode 424)

Given a string s and an integer k, you can replace at most
k characters to make the longest substring contain the 
same character.

Return the length of that longest substring.
'''
s = "AABABBA"
k = 1

# Expected output: 4
def longest_sub_string(s, k):
    freq = {}
    left = 0 
    max_len = 0
    max_freq = 0

    for i in range(len(s)):
        ch = s[i]
        freq[ch] = freq.get(ch, 0) + 1 
        max_freq = max(max_freq, freq[ch])

        while (i - left + 1) - max_freq > k:
            freq[s[left]] -= 1 
            if freq[s[left]] == 0:
                del freq[s[left]]
            left += 1 
        cur_len = (i - left + 1 )
        max_len = max(max_len, cur_len)
    return max_len
print(longest_sub_string(s, k))
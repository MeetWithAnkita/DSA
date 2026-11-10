s = "abcabcbb"

def longest_sub_string_no_repeat(s):
    left = 0 
    max_len = float('-inf')
    freq = {}
    for r in range(len(s)):
        freq[s[r]] = freq.get(s[r], 0) + 1 
        while freq[s[r]] >1:
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                del freq[s[left]]
            left += 1

        current_len = r - left + 1
        max_len = max(max_len, current_len)
    return max_len

print(longest_sub_string_no_repeat(s))
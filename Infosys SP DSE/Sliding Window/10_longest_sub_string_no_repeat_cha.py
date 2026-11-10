s = "pwwkew"

def longest_sub_string(s):
    left = 0 
    max_len = float('-inf')
    freq = {}
    for i in range(len(s)):
        freq[s[i]] = freq.get(s[i], 0) + 1 
        while freq[s[i]] > 1:
            freq[s[left]] -= 1 
            if freq[s[left]] == 0:
                del freq[s[left]] 
            left += 1 
        current_len = i - left + 1 
        max_len = max(max_len, current_len)
    return max_len

        
print(longest_sub_string(s))
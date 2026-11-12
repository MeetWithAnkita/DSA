'''
Problem:
You are given a string s and an integer k.

You can replace at most k characters with any other 
uppercase English character.

Find the length of the longest substring that can be made 
to contain only one repeating character.
'''

s = "ABBBAC"
k = 2

def sub_string(s, k):
    left = 0 
    freq = {}
    max_freq = 0
    max_len = 0 

    for i in range(len(s)):
        freq[s[i]] = freq.get(s[i], 0) + 1 
        max_freq = max(max_freq, freq[s[i]])

        while (i - left + 1) - max_freq > k:
            freq[s[left]] -= 1 
            if freq[s[left]] == 0:
                del freq[s[left]]
            left += 1 
        current_len = (i - left + 1 )
        max_len = max(max_len, current_len)
    return max_len

print(sub_string(s, k))


'''
Complexity
- Time: O(n)
- Auxiliary space: O(1), 
because the character set is limited to 26 uppercase 
English letters.
'''
# Task: Longest Substring Without Repeating Characters
s = "pwwkew"
freq = {}
left = 0 
max_len = 0
max_str = ""
for i in range(len(s)):
    freq[s[i]] = freq.get(s[i], 0) + 1 
    while len(freq) != len(s[left :i+1]):
        freq[s[left]] -= 1 

        if freq[s[left]] == 0:
            del freq[s[left]]
        left += 1 
    curr_len = i - left + 1 
    if max_len < curr_len :
        max_len = curr_len
        max_str = s[left :i+1]
print("Longest Substring: ", max_str)
print("Maximum Length: ", max_len)

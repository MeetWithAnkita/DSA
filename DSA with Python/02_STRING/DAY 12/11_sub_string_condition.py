s = "eceba"
k = 2

left = 0 
freq = {}
max_len = 0 
max_str = ""
for i in range(len(s)):
    freq[s[i]] = freq.get(s[i], 0) + 1 
    while len(freq) > k:
        freq[s[left]] -= 1 
        if freq[s[left]] == 0:
            del freq[s[left]]
        left += 1 
    curr_len = (i - left + 1)
    if max_len < curr_len:
        max_len = curr_len
        max_str = s[left: i+1]
print(max_len)
print(max_str)
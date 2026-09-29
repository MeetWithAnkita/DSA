# Find the length of the longest substring without repeating characters.
s = "abcbb"

left = 0 
freq = {}
max_len = 0 

for r in range(len(s)):
    freq[s[r]] = freq.get(s[r], 0) + 1 

    while freq[s[r]] > 1:
        freq[s[left]] -= 1 

        if freq[s[left]] == 0:
            del freq[s[left]]
        left += 1 
        
    curr_len = r - left + 1
    max_len = max(max_len, curr_len)
                    
print(max_len)




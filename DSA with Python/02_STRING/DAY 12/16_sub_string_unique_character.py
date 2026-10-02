# Task: 
# Print every substring of length k that contains all unique characters.

# s = "aababcabc"
s = "abcabc"
k = 3
left = 0
freq = {}

for i in range(k):
    freq[s[i]] = freq.get(s[i], 0) + 1 
if len(freq) == k:
    print(s[:k])

for i in range(k, len(s)):
    out = s[i-k] 
    freq[out] -= 1 
    if freq[out] == 0:
        del freq[out]
    incoming = s[i]
    freq[incoming] = freq.get(incoming, 0) + 1 

    if len(freq) == k:
        print(s[i-k+1 : i+1])

# fixed-size sliding window with a frequency dictionary.


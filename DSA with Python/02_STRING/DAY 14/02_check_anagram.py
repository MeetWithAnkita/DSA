# 🔤 What is an Anagram?

# Two strings are anagrams if they contain:

# Exactly the same characters
# With exactly the same frequency
# But the order can be different
s = "listen"
t = "silent"

freq = {}
ans = True
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1 
for i in t:
    if i in freq:
        freq[i] -= 1 
        if freq[i] == 0:
            del freq[i]
    else:
        ans = False
        break
if freq:
    ans = False 

print(ans)


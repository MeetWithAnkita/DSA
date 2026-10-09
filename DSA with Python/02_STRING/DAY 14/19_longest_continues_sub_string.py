# Task: 
# We need the longest continuous substring with no repeated characters.

s = "aabccdeff"
max_str = ""
max_len = 0
seen = set()
left = 0

for right in range(len(s)):
    while s[right] in seen:
        seen.remove(s[left])
        left += 1
    seen.add(s[right])
    curr_len = (right - left + 1) 
    # if len(seen) == curr_len:
    if curr_len > max_len:
        max_len = curr_len
        max_str = s[left: right+1]

print(max_str, "   ", max_len)



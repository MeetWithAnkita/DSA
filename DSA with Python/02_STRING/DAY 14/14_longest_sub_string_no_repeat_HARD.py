s = "abcabcbb"

seen = set()
left = 0
max_len = 0
max_str = ""

for right in range(len(s)):

    # If current character already exists,
    # remove characters from the left
    while s[right] in seen:
        seen.remove(s[left])
        left += 1

    seen.add(s[right])

    current_len = right - left + 1

    if current_len > max_len:
        max_len = current_len
        max_str = s[left: right+1]

print("Max Len:", max_len)
print("Max str:", max_str)

# implemented the standard Sliding Window + Set solution.

# Task: Find the length of the longest substring containing at most k distinct characters.
s = "aabacbebebe"
k = 2

left = 0
freq= {}
max_len = 0 
max_str = ""

for r in range(len(s)):
    freq[s[r]] = freq.get(s[r], 0) + 1

    while len(freq) > k:
        freq[s[left]] -= 1

        if freq[s[left]] == 0:
            del freq[s[left]]
        left += 1

    curr_len = r - left + 1
    # max_len = max(max_len, curr_len)
    if curr_len > max_len:
        max_len = curr_len
        max_str = s[left: r+1]

print(max_len)
print(max_str)


# | Complexity     | Result                       |
# | -------------- | -----------------------------|
# | **Time**       | ⭐ **O(n)**                 |
# | **Space**      | ⭐ **O(k)**                 |
# | Two pointers   | `left`, `right`              |
# | Main technique | Variable-size Sliding Window |


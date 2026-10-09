s = "babad"
max_pall = ""
max_len = 0 

for i in range(len(s)):
    # s = 0 1 2 3 4 5 
    # ////////// Odd Length Pallindrome //////////
    left = i
    right = i 
    while left >= 0 and right < len(s) and s[left] == s[right]:
        if right - left + 1 > max_len:
            max_len = right - left + 1 
            max_pall = s[left : right+1] 
        left -= 1  
        right += 1 
    # /////////// Even Length Pallindrome //////////
    left = i 
    right = i + 1
    while left >= 0 and right < len(s) and s[left] == s[right]:
        if right - left + 1 > max_len:
            max_len = right - left + 1 
            max_pall = s[left : right+1] 
        left -= 1 
        right += 1 

print("Max Pallindrome: ", max_pall)
print("Max Length: ", max_len)


# Complexity
# Time: O(n²)
# Space: O(1) extra space (excluding the returned substring)

# I got the expand-around-center idea.
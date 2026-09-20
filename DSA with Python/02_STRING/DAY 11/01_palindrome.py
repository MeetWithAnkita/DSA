# Rules

# For this first question:

# Don't use s[::-1]
# Use ======>.....[Two Pointer]
# Use while
# Compare characters from both ends.

s = "racecar"
l = 0
r = len(s) - 1
p = True

while l < r:
    if s[l] == s[r]:
        l += 1 
        r -= 1 
    else:
        p = False
        break
if p:
    print("Pallindrome")
else: 
    print("Not Palindrome")

# Complexity

# Time: O(n)
# Extra Space: O(1) ✅

s = "Madam"
s = s.lower()
l = 0
r = len(s) - 1 
p = True 
while l < r :
    if s[l] == s[r]:
        l += 1 
        r -= 1 
    else:
        p = False 
        break
if p:
    print("Pallindrome")
else: 
    print("Not Pallindrome")


# Complexity
# lower() → O(n)
# Two-pointer scan → O(n)
# Overall: O(n) time
# Extra space: O(n) because lower() creates a new string.
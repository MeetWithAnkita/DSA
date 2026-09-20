# s = "nurses run"
s = "Never Odd Or Even"
s = s.replace(" ","")
s = s.lower()
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
    print("Palindrome")
else: 
    print("Not Palindrome")

# Preprocessing: O(n)
# Two-pointer comparison: O(n)
# Overall: O(n) time
# Extra space: O(n) due to creating the processed string.
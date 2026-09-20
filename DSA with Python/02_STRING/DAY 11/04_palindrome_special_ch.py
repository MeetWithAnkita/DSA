# Treat only letters and digits as meaningful.

# Ignore:

# spaces
# commas ,
# colon :
# other punctuation
# uppercase/lowercase differences

s = "A man, a plan, a canal: Panama"
s = s.lower()

for i in s:
    if not i.isalnum() :
        s = s.replace(i, "")

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

# | Part             |                 Time | Extra Space |
# | ---------------- | -------------------: | ----------: |
# | `lower()`        |                 O(n) |        O(n) |
# | `replace()` loop | **O(n²)** worst case |        O(n) |
# | Two pointers     |                 O(n) |        O(1) |
# | **Overall**      |            **O(n²)** |    **O(n)** |


    
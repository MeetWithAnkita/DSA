# s = "3[a]2[bc]"

# Construct the decoded string.

# Expected: aaabcbc

# Meaning:

# 3[a]  → aaa
# 2[bc] → bcbc

# Result → aaabcbc

s = "3[a]12[bc]"
no = []
n1 = 0
n2 = 0
stack = []

for i in range(len(s)):
    if s[i].isdigit():
        no.append(s[i])
    if s[i] == "[":
        n1 = i
    if s[i] == "]":
        n2 = i
        # stack.append(int( s[(n1-1)] ) * s[n1+1 : n2])
        number = int("".join(no))
        stack.append(number * s[(n1+1) : n2])
        no.clear()
        

print("".join(stack))




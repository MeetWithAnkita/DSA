s = "abbaca"
# Task: 
# Whenever two adjacent characters are the same, remove them.
stack = []
for ch in s:
    if not stack or stack[-1] != ch:
        stack.append(ch)
    else:
        stack.pop()
print("".join(stack))
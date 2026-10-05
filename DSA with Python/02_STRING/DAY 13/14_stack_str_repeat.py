# Task:
# Use a stack to construct the final string.
# Don't use: s * k
# Try to build it using append() / pop() or another stack-based approach.

s = "abc"
k = len(s)
stack = []
i = 0 
while i<k:
    for ch in s:
        stack.append(ch)
    i += 1
print("".join(stack))
        



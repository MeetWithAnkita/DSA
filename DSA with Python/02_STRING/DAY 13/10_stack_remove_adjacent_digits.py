s = "aabbccd"

stack = []
for ch in s:
    if not stack:
        stack.append(ch)
    else:
        if stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)
print(" ".join(stack))
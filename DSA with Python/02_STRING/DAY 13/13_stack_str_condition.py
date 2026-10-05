s = "leet**cod*e"
# task:
# Remove the * character immediately before it from the current result.
stack = [] 
for ch in s:
    if ch != "*":
        stack.append(ch)
    else:
        stack.pop()
print("".join(stack))
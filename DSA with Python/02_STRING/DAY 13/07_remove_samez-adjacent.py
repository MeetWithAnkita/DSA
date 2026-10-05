s = "abbacaac"
# Task:
# Whenever two adjacent characters become equal, remove them.

stack= []

for ch in s:
    if not stack:
        stack.append(ch)
    else:
        if ch != stack[-1]:
            stack.append(ch)
        else:
            stack.pop()
print("".join(stack))

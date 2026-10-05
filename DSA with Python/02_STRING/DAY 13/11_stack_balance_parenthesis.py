s = "(((()))"

stack = []
f = True
for ch in s:
    if ch == "(":
        stack.append(ch)
    else:
        if not stack:
            f = False 
            break
        stack.pop()
else:
    if not stack:
        print("True")
    else:
        print("False")


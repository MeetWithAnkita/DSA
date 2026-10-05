# Task:
# Check whether all brackets are balanced.

s = "a{b[c(d)e]f}g"
f = True
stack = []

for i in s:
    if i in "{[(":
        stack.append(i)
    else:
        if i in "}])":
            if not stack:
                f = False 
                break 
            else: 
                if (i == "}" and stack[-1] == "{")or \
                   (i == ")" and stack[-1] == "(")or \
                   (i == "]" and stack[-1] == "["):
                    stack.pop()
                else:
                    f = False 
                    break 
if stack:
    f = False

print(f)

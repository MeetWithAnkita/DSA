# s = "{[()]}"
s = "{[(])}"
stack = []
f = True

for ch in s:
    if ch in "{[(":
        stack.append(ch)
    else:
        if not stack:
            f = False 
            break
        else: 
            if ch == "}" and stack[-1] == "{" or\
            ch == "]" and stack[-1] == "[" or\
            ch == ")" and stack[-1] == "(" :
                stack.pop()
            else:
                f = False
                break

if f and not stack:
    print("True")
else:
    print("False")



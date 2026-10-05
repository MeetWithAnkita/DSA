s = "a2b3c"

al = ""
no = 0 
stack = []

for ch in s:
    if ch.isdigit():
        no = no * 10 + int(ch)
    else:
        if al:
            if no:
                stack.append(al * no)
            else:
                stack.append(al)
        al = ch 
        no = 0 
if al:
    if no:
        stack.append(al * no)
    else:
        stack.append(al)

print("".join(stack))


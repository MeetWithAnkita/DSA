s = "3[a2[c]]"
# 3[a cc]
# acc acc acc

no = 0
cur = ""
stack = []

for ch in s:
    if ch.isdigit():
        no = (no * 10) + int(ch)
    elif ch == "[":
        stack.append((no, cur))
        no = 0
        cur = ""
    elif ch == "]":
        repeat, previous = stack.pop()
        cur = previous + cur * repeat 
    else:
        cur += ch 
print(cur)





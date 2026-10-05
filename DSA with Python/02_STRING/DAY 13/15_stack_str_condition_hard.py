# Task:
# Each character is followed by its repetition count.
# Expected output:
# aaabbc

# s = "a3b2c"
s = "a3bc2d"
stack = []
al = ""
no = 0

for ch in s:
    if ch.isdigit():
            no = no*10 + int(ch) 

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
    
    

    


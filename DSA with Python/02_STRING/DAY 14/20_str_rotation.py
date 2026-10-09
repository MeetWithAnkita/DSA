s_str = "abcd"
s = list(s_str)
t = "cdab"
# Task:
# Determine whether t is a rotation of s.
k = 0
left = 0 

while k < len(s):
    store = s[len(s)-1]
    for right in range(len(s)-2, -1, -1):
        s[(right + 1)] = s[right]
    s[0] = store
    if ("".join(s)) == t:
        print("True")
        break

    k += 1
else:
    print("False")




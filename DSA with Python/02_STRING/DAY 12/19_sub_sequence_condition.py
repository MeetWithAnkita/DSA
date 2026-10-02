# s = "abcde"
s = "abedc"
target = "ace"

i = 0
j = 0 

while i < len(s) and j < len(target):
    if s[i] == target[j]:
        j += 1 
    i += 1 
if j == len(target):
    print("True")
else:
    print("False")





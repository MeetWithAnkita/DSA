# Input: PyTHon Is Fun
# Output: 5

s = "PyTHon Is Fun12345"
c = 0
d = 0
for i in s:
    if i.isupper():
        c += 1 
    if i.isdigit():
        d += 1
print("Uppercase: ",c) 
print("Digit: ", d)
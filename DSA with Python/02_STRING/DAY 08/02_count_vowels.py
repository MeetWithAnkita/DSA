word = input("String: ")
v = 0 
for i in word:
    if i in "aeiouAEIOU":
        v += 1 
print(v)

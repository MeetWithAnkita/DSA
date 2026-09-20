s1 = "listen"
s2 = "silent"

freq = {}
a = True

for i in s1:
    freq[i] = freq.get(i, 0) + 1 

for i in s2:
    if i in freq:
        freq[i] -= 1
    else:
        a = False
        break

# Every frequency must be 0
if a:
    for value in freq.values():
        if value != 0:
            a = False 
            break


if a:
    print("Anagram")
else:
    print("Not Anagram")

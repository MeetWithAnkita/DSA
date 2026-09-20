s1 = "rail safety"
s2 = "fairy tales"
s1_set = s1.replace(" ", "")
s2_set = s2.replace(" ", "")


freq= {}
a = True
for i in s1_set:
    freq[i] = freq.get(i, 0) + 1 

for i in s2_set:
    if i in freq:
        freq[i] -= 1 
    else:
        a = False
        break
if a:
    for value in freq.values():
        if value != 0:
            a = False
if a:
    print("Anagram")
else:
    print("Not Anagram")


# ////////////    2nd Way     ////////////
s1 = "rail safety"
s2 = "fairy tales"

freq = {}
a = True

for i in s1:
    if not i.isspace():
        freq[i] = freq.get(i, 0) + 1

for i in s2:
    if not i.isspace():
        if i in freq:
            freq[i] -= 1
        else:
            a = False
            break

if a:
    for value in freq.values():
        if value != 0:
            a = False
            break

if a:
    print("Anagram")
else:
    print("Not Anagram")


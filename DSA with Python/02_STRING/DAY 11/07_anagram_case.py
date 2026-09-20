s1 = "Listen"
s2 = "Silent"
s1 = s1.lower()
s2 = s2.lower()

freq = {}
a = True
for i in s1:
    freq[i] = freq.get(i, 0 ) + 1 

for i in s2:
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


# Complexity

# Let n = len(s1), m = len(s2):

# Time: O(n + m)
# Space: O(k), where k = distinct characters.
# Example: words starting with a vowel, ending with "ing", length > 4, etc.

s = "eating meeting sitting ing"
w = s.split()
v = "aeiouAEIOU"
for i in w: 
    if i.endswith("ing"):
        if len(i) > 4:
            if i[0] in v:
                print(i)

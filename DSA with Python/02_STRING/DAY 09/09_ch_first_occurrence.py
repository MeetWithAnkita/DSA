s = "programming"
ch = "g"

for i in range(len(s)): 
    if s[i] == ch:
        print("Index: ",i)
        break
print("INDEX: ", s.find(ch))
print("Count g: ", s.count(ch))
# Task: Count how many words end with "ing".
s = "I am learning Python and solving problems"
count = 0
w = s.split()
for i in w:
    if i.endswith("ing"):
        count += 1
print("Count: ",count)
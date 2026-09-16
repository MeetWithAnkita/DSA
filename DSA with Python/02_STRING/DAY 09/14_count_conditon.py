# Task: Count how many words start with "p" or "P".
s = "Python is powerful and Python is popular"
w = s.split()
count = 0 
for i in w: 
    if i.startswith("p") or i.startswith("P"):
        count += 1
print("Count: ", count)
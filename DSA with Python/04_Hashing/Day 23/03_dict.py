marks = {
    "Python": 85,
    "SQL": 90,
    "Java": 75
}

# 1. Print the Python marks.
print(marks["Python"])

# 2. Add "DSA" with marks 95.
marks["DSA"] = 95

# 3. Update Java marks to 80.
marks["Java"] = 80

# 4. Check whether "SQL" exists.
print("SQL" in marks)           #Checks whether "SQL" exists as a key.
print(90 in marks.values())     #Checks whether 90 exists as a value.

# 5. Print all subjects and marks using a loop.
for k, v in marks.items():
    print(k, v)


freq1 = {20:1} 
freq1.setdefault(10, 0)
print(freq1)
freq1[10] += 1 

print(freq1)

freq1[10] -= 2
freq1[20] -= 2
print(freq1)
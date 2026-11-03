arr = [1, 2, 3, 2, 4, 3, 5, 1]

seen = set()
duplicates = set()

for i in arr:
    if i in seen:
        duplicates.add(i)
    else:
        seen.add(i)

print(duplicates)
print(seen)
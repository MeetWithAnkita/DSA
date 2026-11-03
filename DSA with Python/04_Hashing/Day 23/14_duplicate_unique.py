arr = [4, 2, 7, 2, 8, 4, 9, 2, 7, 5]

unique = set()
duplicate = set()

for i in arr:
    # if i not in unique:
    #     if i not in duplicate:
    #         unique.add(i)
    # elif i in unique:
    #     duplicate.add(i)
    #     unique.remove(i)
    if i in duplicate:
        continue
    elif i in unique:
        unique.remove(i)
        duplicate.add(i)
    else:
        unique.add(i)


print("Duplicates: ", duplicate)
print("Unique Element: ", unique)


arr = [2, 7, 11, 15]
target = 9

found = False
for i in arr:
    if (target - i) in arr:
        found = True 
        break 
print(found)

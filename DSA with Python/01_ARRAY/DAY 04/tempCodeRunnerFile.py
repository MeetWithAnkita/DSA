arr = [12, 25, 7, 40, 18, 30]
target = 50

found = False 
index = 0
for i in range(len(arr)):
    if arr[i] == target:
        found = True 
        index = i
        break
if found: 
    print("Found, Index: ", index)
else: 
    print("Not Found, Index: -1")
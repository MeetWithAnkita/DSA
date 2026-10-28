arr = [2, 5, 2, 7, 2, 9, 5]
target = 2

count = 0 
for i in range(len(arr)):
    if target == arr[i]:
        count += 1 
print(count)
arr = [9, 12, 3, 5, 14, 7, 2, 10]
pivot = 7 
pos = 0

for i in range(len(arr)):
    if arr[i] < pivot:
        arr[pos], arr[i] = arr[i], arr[pos]
        pos += 1 
for i in range(len(arr)):
    if arr[i] == pivot:
        arr[pos], arr[i] = arr[i], arr[pos]
        break
print(arr)

# Time:  O(n) ✅
# Space: O(1) ✅
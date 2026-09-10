arr = [3, -2, 5, -7, 8, -1]
position = 0 
for i in range(len(arr)):
    if arr[i] < 0:
        arr[position], arr[i] = arr[i], arr[position]
        position += 1 
print(arr)

# Complexity
# Time: O(n) — one traversal
# Extra Space: O(1) — only position and i
# In-place: ✅ Yes
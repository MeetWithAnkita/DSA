arr = [0, 5, 0, 3, 2, 0, 8]
# Move all zeros to the end, while maintaining the order of non-zero elements.
# Expected: [5, 3, 2, 8, 0, 0, 0]

position = 0 
for i in range(len(arr)):
    if arr[i] != 0:
        arr[position] , arr[i] = arr[i], arr[position]
        position += 1
print(arr)

# Complexity	Your solution
# Time	O(n) ✅
# Extra Space	O(1) ✅
# In-place	Yes ✅
# Preserves non-zero order	Yes ✅
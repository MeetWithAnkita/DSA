arr = [0, 1, 0, 3, 12]
# for i in range(len(arr)-1):
#     for j in range(i + 1, len(arr)):
#         if arr[i] == 0 and arr[j] != 0:
#             arr[i], arr[j] = arr[j], arr[i]

# Time: O(n²)
# Extra Space: O(1)

position = 0 
for i in range(len(arr)):
    if arr[i] != 0 :
        arr[position] = arr[i]
        arr[i] = 0
        position += 1
# Complexity
# Time: O(n)
# Extra Space: O(1)
# Stable order: ✅
print(arr)

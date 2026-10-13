arr = [0, 1, 0, 3, 12]

# for i in range(len(arr)):
#     for j in range(i + 1, len(arr)):
#         if arr[i] == 0 and arr[j] != 0:
#             arr[i], arr[j] = arr[j], arr[i]
# print(arr)

z = 0 
for i in range(1, len(arr)):
    if arr[i] != 0:
        arr[z], arr[i] = arr[i], arr[z]
        z += 1 
print(arr)


# Task:
# Rotate Array Right by k.
arr = [1, 2, 3, 4, 5]
k = 2

# arr1 = arr[len(arr) - 2 : ]
# print(arr1 + arr[: len(arr) - 2])
k2 = 0
while k2 < k:
    var = arr[len(arr) -1]
    for i in range(len(arr)-1, -1, -1):
        arr[i] = arr[i - 1]
    arr[0] = var
    k2 += 1
print(arr)



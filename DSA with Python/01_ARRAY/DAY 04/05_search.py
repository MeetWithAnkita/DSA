# Task: Find the first even number and print its index and value.

arr = [11, 15, 21, 8, 17, 24, 30]

for i in range(len(arr)):
    if arr[i] % 2 == 0 :
        print("Index: ", i)
        print("Value: ", arr[i])
        break 
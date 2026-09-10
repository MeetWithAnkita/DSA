# Task: Find the first element greater than 20 and print its index and value.

arr = [12, 7, 25, 18, 30, 9, 40]
for i in range(len(arr)):
    if arr[i] > 20:
        print("Index: ", i)
        print("Value: ", arr[i])
        break
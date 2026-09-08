# arr = list(map(int, input("Array Element: ").split()))
arr = [10, 20, 30, 40, 50]
print(arr)

print("First element: ",arr[0])

arr.append(100)
print(arr)

print(arr.pop(1))
print(arr)

arr.insert(3, 150)
print(arr)

arr.remove(150)
print(arr)

arr[4] = 300
print(arr)


for i in arr:
    print(i)

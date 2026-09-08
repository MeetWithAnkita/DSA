arr = [10, 45, 23, 67, 12]
print("Maximum Element: ", max(arr))
print("Minimum Element: ", min(arr))

minimum = arr[0]
maximum = arr[0]
for i in range(len(arr)): 
    if minimum > arr[i]:
        minimum = arr[i]
    if maximum < arr[i]:
        maximum = arr[i]
print("Minimum: ", minimum )
print("Maximum: ", maximum)
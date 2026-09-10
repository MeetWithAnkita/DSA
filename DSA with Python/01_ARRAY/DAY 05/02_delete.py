arr = [10, 20, 30, 40, 50]
position = 2

# pop() delete element using index + value 
# remove() delete element using value only.

for i in range(position, len(arr)-1):
    arr[i] = arr[i + 1]
arr.pop()
print(arr)

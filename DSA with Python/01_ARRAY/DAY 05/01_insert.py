arr = [10, 20, 30, 40, 50]
# We want to insert: 
Value = 15 #25
position = 1 #2

# have to add a new extra place to swipe element left to right 
arr.append(0)

for i in range(len(arr)-1, position, -1 ):
    arr[i] = arr[i - 1]
arr[position] = Value
print(arr)
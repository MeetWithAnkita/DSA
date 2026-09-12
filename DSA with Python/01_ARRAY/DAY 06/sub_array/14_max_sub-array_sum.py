arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# find the maximum possible sum of any contiguous subarray.

max_total = float('-inf')

for i in range(len(arr)):
    total = 0
    for j in range(i, len(arr)):
        total += arr[j]
        print(i,j,"-->",arr[i:j+1],"-->",total)
        if max_total < total:
            max_total = total 
print("Maximum subarray sum: ", max_total)

# Complexity
# Complexity	|| Value
# Time	        || O(n²)
# Extra Space	|| O(1)

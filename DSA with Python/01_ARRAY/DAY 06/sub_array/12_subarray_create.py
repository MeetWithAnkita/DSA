arr = [1, 2, 3]

for i in range(len(arr)):
    for j in range(i, len(arr)):
        print(i,j,"-->", arr[i:j+1])

# Complexity

# For an array of n elements:

# Number of subarrays = n × (n + 1) / 2
# So there are O(n²) subarrays.
# Because we're also creating/printing each subarray,
#  the total work can be O(n³) in the worst case.
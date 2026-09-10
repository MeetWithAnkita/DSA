arr = [1, 2, 3, 4, 5]
k = 2
# Rotate the array 2 positions to the right.
count = 1
while count <= k:
    last = arr[len(arr) - 1]
    for i in range(len(arr)-1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = last
    count += 1
print(arr)


# Complexity

# For k rotations:

# Time: O(n × k)
# Extra Space: O(1)

# For example, if n = 5 and k = 2, roughly 5 × 2 operations.

# 💡 Important: This is the straightforward method. Later, we'll learn an optimized rotation technique that can achieve O(n) time even when k is large.
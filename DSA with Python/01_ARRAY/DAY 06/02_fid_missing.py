# Given an array containing numbers from 1 to n, with exactly one number missing:
# Find missing ones

arr = [1, 2, 4, 5, 6]
n = arr[len(arr) - 1]
total = 0
expected_sum = (n*(n+1))//2
for i in arr:
    total += i
print("Mising No: ", (expected_sum - total))

# Time: O(n) — one traversal to calculate the actual sum.
# Extra Space: O(1) — only variables are used.
# In-place: Yes, we don't modify the array.
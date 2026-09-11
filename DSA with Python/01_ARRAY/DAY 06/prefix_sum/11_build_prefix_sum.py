arr = [2, 4, 1, 5, 3]
# Task: Create a new array containing the prefix sums.

total = 0
arr2 = []
for i in arr:
    total += i
    arr2.append(total)
print(arr2)

# Complexity
# Time: O(n)
# Extra Space: O(n) because we're creating a new prefix array.

# Task: Then find the sum of elements from index 2 to index 5 using the prefix sum.
L = 2
R = 4
total14 = arr2[R] - arr2[L - 1]
print(total14)


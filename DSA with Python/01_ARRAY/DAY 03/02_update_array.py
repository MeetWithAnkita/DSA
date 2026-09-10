arr = list(map(int, input().split()))

for i, value in enumerate(arr):
    arr[i] = 2 * value
print("Updated list: ",arr)


# Complexity
# Time: O(n) ✅
# Extra Space: O(1) ✅
# In-place modification: ✅

# reverse traversal 
print("Reverse Traversal: ", arr[::-1])
# arr[::-1] creates a new reversed list, so it uses O(n) extra space.

for i in range((len(arr) - 1), -1, -1): 
    print(arr[i])

# Time: O(n)
# Extra Space: O(1) ✅

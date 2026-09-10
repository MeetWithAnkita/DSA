# Task: Add 5 to every element that is greater than 10.

arr = [5, 12, 7, 20, 9, 30]
for i in range(len(arr)):
    if arr[i] > 10 :
        arr[i] += 5
print(arr)

# Complexity
# Time: O(n) ✅
# Extra Space: O(1) ✅
# In-place: ✅
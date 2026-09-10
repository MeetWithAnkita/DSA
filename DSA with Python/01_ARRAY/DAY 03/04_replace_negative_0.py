# Task: Replace every negative number with 0.
# 2> Count how many negative numbers were present
arr = [10, -5, 20, -8, 30, -2]
count = 0 
for i in range(len(arr)):
    if arr[i] < 0:
        arr[i] = 0 
        count += 1 
print("Updated Array: ",arr)
print("Negative numbers: ", count)

# Complexity
# Time: O(n) ✅
# Extra Space: O(1) ✅
# In-place modification: ✅
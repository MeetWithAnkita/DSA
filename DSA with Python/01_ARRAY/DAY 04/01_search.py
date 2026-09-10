arr = [12, 25, 7, 40, 18, 30]
target = 40

for i in range(len(arr)):
    if target == arr[i]:
        print("Index: ", i)
        break
# Complexity
# Worst-case Time: O(n) ✅
# Best-case Time: O(1) ⭐
# Extra Space: O(1) ✅
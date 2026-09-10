# Task: 
# 1> If the element is even, multiply it by 2.
# 2> If the element is odd, add 1.
# 3> Count how many even numbers were originally present.

arr = list(map(int, input().split()))
count_e = 0 
for i, value in enumerate(arr):
    if value % 2 == 0 :
        arr[i] = value * 2 
        count_e += 1 
    else: 
        arr[i] += 1 
print("Updated Array: ", arr)
print("Even Numbers: ", count_e)

# Complexity
# Time: O(n)
# Extra Space: O(1)
# In-place: ✅
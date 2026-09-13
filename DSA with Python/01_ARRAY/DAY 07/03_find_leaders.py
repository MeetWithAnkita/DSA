# Task: 
# An element is called a leader if it is greater than all elements to its right.

arr = [16, 17, 4, 3, 5, 2]
pos = 0
while pos < len(arr):
    is_leader = True
    for i in range(pos+1, len(arr)):
        if arr[pos] <= arr[i]:
            is_leader = False
            break
    if is_leader:
        print(arr[pos]) 
    pos += 1



# ////////////////// 2 ND WAY ////////////////////
# arr = [16, 17, 4, 3, 5, 2]
# max_ele = float('-inf')

# for i in range(len(arr)-1, -1, -1):
#     if arr[i] > max_ele:
#         print(arr[i]) 
#         max_ele = arr[i]

# # Time = O(n)
# # Extra Space = O(1)
# Approach	Time	Extra Space
# Your nested-loop approach	O(n²)	O(1)
# Right → Left + max_right ⭐	O(n)	O(1)
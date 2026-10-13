# arr = [16, 17, 4, 3, 5, 2]

# A leader is an element that is greater than or equal to every element to its right. The last element is always a leader.
# pos = 0
# while pos < len(arr):
#     res = True
#     for i in range(pos+1, len(arr)):
#         if arr[pos] <= arr[i]:
#             res = False
#             break
#     if res:
#         print(arr[pos])
#     pos += 1 
arr = [16, 17, 4, 3, 5, 2]

max_right = float('-inf') 
leaders = []

for i in range(len(arr)-1, -1, -1):
    if arr[i] >= max_right:
        leaders.append(arr[i])
        max_right = arr[i]
leaders.reverse()
print(leaders)




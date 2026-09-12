# # You just solved Maximum Subarray Sum using brute force O(n²).

# # Now we want to solve the same problem in O(n).

# arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# max_total = float('-inf')

# position = 0 
# while position < len(arr):
#     total = 0
#     for i in range(position, len(arr)):
#         total += arr[i]
#         print(position,i,"-->",arr[position:i+1],"-->",total)
#         if total > max_total:
#             max_total = total
#     position += 1 
# print("Max: ", max_total)

# arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
arr = [4, -1, 2, 1, -5]
total = 0
max_sum = float('-inf')

for i in range(len(arr)):

    # YOUR LOGIC HERE
    total += arr[i]
    if total < arr[i]:
        total = arr[i] 
    if total > max_sum:
        max_sum = total
# No    total=0     max
# -2    -2          -2 
# 1     -1-> 1      1
# -3    -2          1
# 4     2 -> 4      4
# -1    3           4
# 2     5           5
# 1     6           6
# -5    1           6
# 4     5           6


print("Maximum subarray sum:", max_sum)

# The key rule of Kadane is:
# If the previous accumulated sum hurts the current element, 
# drop it and start a new subarray.




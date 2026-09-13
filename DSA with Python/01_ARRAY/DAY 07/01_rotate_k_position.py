# arr = [1, 2, 3, 4, 5, 6, 7]
# k = 3
# count = 0 
# temp = 0 
# while count < k:
#     temp = arr[len(arr) - 1]
#     for i in range(len(arr)-1, 0, -1):
#         arr[i] = arr[i-1]
#     arr[0] = temp
#     count += 1
# print(arr)
# 
# Time Complexity: O(n * k)


# ////////////////// 2 ND WAY ////////////////////

# arr = [1, 2, 3, 4, 5, 6, 7]
# k = 3

# # arr2 = arr[k+1:]
# print(arr[k+1:] + arr[:k+1])

# Time: O(n)
# space: O(n)

# ////////////////// 3 RD WAY ////////////////////

arr = [1, 2, 3, 4, 5, 6, 7]
k = 3

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1 
n = len(arr)
k = k % n 

# 1st step
reverse(arr, 0, n-1)

# 2nd step 
reverse(arr, 0, k-1)

# 3rd step 
reverse(arr, k, n-1)

print(arr)


# Complexity:
# Time → O(n)
# Extra Space → O(1) ======> BEST OPTIMAL SOLUTION 
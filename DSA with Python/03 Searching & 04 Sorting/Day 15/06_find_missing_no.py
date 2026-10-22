arr = [1, 2, 4, 5, 6, 7]
n = len(arr) + 1
# total = n * (n+1) // 2
# t = 0
# for i in arr:
#     t += i 
# print(total - t )


# for i in range(1, n+1):
#     if i not in arr:
#         print("Missing no: ", i)


def find_missing(arr):
    n = len(arr) + 1 
    for i in range(1, n+1):
        if i not in arr:
            return i
    return - 1 

print(find_missing(arr))


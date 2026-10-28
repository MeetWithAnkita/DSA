# arr = [8, 15, 23, 6, 19]
# target = 6

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1 
print(linear_search([12, 7, 12, 5, 12, 9], 12))
print(linear_search([8, 15, 23, 6, 19], 6))
print(linear_search([8, 15, 23, 6, 19], 100))
print(linear_search([5, 8, 3, 8, 2, 8], 8))


# break → exit the loop.
# return → exit the function.
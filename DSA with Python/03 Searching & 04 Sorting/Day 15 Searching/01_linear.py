# # Without Function use 
# arr = [12, 25, 7, 40, 18]
# target = 40

# for i in range(len(arr)):
#     if arr[i] == target:
#         print(f"Found at index: {i}")
#         break 


# Using Function 
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i 
            break
    return -1 

print(linear_search([12, 25, 7, 40, 18], 40))
print(linear_search([12, 25, 7, 40, 18], 99))
# # arr = [10, 20, 20, 30, 40, 40]

# # Find the:
# # Largest distinct element
# # Second largest distinct element
# # Smallest distinct element
# # Second smallest distinct element


# arr = [10, 20, 20, 30, 40, 40]
# arr = set(arr)
# arr = list(arr)
# print(arr)

# small = float('inf')
# small_2 = float('inf')
# large = float('-inf')
# large_2 = float('-inf')

# for i in arr :
#     if i > large:
#         large_2 = large 
#         large = i 
#     elif i > large_2:
#         large_2 = i 
#     if i < small:
#         small_2 = small 
#         small = i 
#     elif i < small_2 :
#         small_2 = i 
# print("Largest distinct element: ", large)
# print("Second largest distinct element: ", large_2)
# print("Smallest distinct element: ", small)
# print("Second smallest distinct element: ", small_2)


# ///////////////////////////
# without set() and without creating another array, you can remove duplicates in-place.
# ///////////////////////////
arr = [10, 20, 20, 30, 40, 40]
i = 0
while i < len(arr):
    j = i+1
    while j < len(arr):
        if arr[i] == arr[j]:
            arr.pop(j)
        else:
            j += 1 
    i += 1 

print(arr)        


# ////////////////// 
# you don't actually need to create a distinct array at all. 
# ///////// Lets try/////////

arr = [10, 20, 20, 30, 40, 40]
small = float('inf')
small_2 = float('inf')
large = float('-inf')
large_2 = float('-inf')

for i in arr :
    if i > large: #large = 10 => 20
        large_2 = large  #large_2 = 10
        large = i 
    elif i > large_2 and i != large: 
        large_2 = i 
    # elif i > large_2 and i != large:
    #     pass
    if i < small: #small = 10 
        small_2 = small 
        small = i 
    elif i < small_2 and i != small: #small_2 = 20
        small_2 = i 
    # elif i != small and i != small_2 :
    #     pass
print("Largest distinct element: ", large)
print("Second largest distinct element: ", large_2)
print("Smallest distinct element: ", small)
print("Second smallest distinct element: ", small_2)





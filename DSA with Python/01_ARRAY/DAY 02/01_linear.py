arr = [10, 25, 30, 45, 50]
target = 100 

# for i, value in enumerate(arr):
#     if value == target:
#         print("Found")
#         break
#     if i == (len(arr)-1):
#         print("Not Found")

# Time: O(n)
# Space: O(1)
found = False
for i, value in enumerate(arr):
    if value == target:
        found = True
        print("Index: ",i)
        break

if found :
    # print("Found")
    pass
else:
    print("Not Found, Index = -1")
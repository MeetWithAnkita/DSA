# 2. Second Smallest Distinct Element
# Find the second-smallest distinct element without sorting.
# arr = [4, 2, 7, 2, 1] → 2
arr = [4, 2, 7, 2, 1]

small = float('inf')
small_2 = float('inf')
for i in arr:
    if i < small:
        small_2 = small 
        small = i
    elif i < small_2 and i != small:
        small_2 = i
print(small_2)


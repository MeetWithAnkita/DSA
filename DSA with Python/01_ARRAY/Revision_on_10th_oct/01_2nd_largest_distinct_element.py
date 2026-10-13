# 1. Second Largest Distinct Element
# Find the second-largest distinct element without sorting the array.
# arr = [10, 5, 20, 8, 20] → 10

# arr = [10, 5, 20, 8, 20]
arr = [-5, -2, -10, -2]
large = float('-inf')
s_large = float('-inf')
for i in arr:
    if i > large:
        s_large = large 
        large = i
    elif i > s_large and i != large:
        s_large = i
print(s_large)

# large = 10 , 20
# s_large = 0 , 5, 10

    
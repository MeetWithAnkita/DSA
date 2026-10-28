# 1. What is Selection Sort?
# Selection Sort repeatedly selects the smallest element 
# from the unsorted portion and places it in its correct 
# position.

# The key idea:
# 1. Find the minimum element.
# 2. Swap it with the first element of the unsorted portion.
# 3. Move to the next position.
# 4. Repeat until sorted.

# Remember the difference:
# - Bubble Sort → compares adjacent elements and swaps.
# - Selection Sort → finds the minimum element and swaps it into position.


arr = [5, 3, 8, 2, 4]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        # print(arr)

    return arr


print(selection_sort(arr))



# Complexity	    Your code
# =============================
# Best time	        O(n²)
# Average time	    O(n²)
# Worst time	    O(n²)
# Auxiliary space	O(1)
# In-place	        Yes
# What is Quick Sort?
# Quick Sort is a Divide and Conquer sorting algorithm.

# It works by:
# 1. Choosing one element as a pivot.
# 2. Partitioning the array around the pivot.
# 3. Placing smaller elements on the left and larger elements on the right.
# 4. Recursively sorting the left and right portions.

# Case	    Time complexity
# Best	    O(n log n)
# Average	O(n log n)
# Worst	    O(n²)
# Auxiliary space	O(log n) average recursion stack; 
#                   O(n) worst


# arr = [8, 3, 6, 2, 9, 4]
arr = [10, 7, 8, 9, 1, 5, 5]

def partition(arr, low, high):
    pivot = arr[high]
    i  = low - 1 
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1 
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    print(arr)
    return i + 1


def quick_sort(arr, low, high):

    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)
    return arr

print(quick_sort(arr, 0, len(arr) -1))

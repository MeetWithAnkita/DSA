arr = [6, 3, 8, 1]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # print(arr)

        if not swapped:
            break
    return arr


print(bubble_sort(arr))


# - Best-case time: O(n) — already sorted.
# - Average-case time: O(n²).
# - Worst-case time: O(n²).
# - Auxiliary space: O(1).
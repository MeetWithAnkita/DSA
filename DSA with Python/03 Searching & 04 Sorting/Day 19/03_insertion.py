arr = [9, 5, 7, 3]


def insertion_sort(arr):
    n = len(arr) 
    for i in range(1, n):
        key = arr[i]
        j = i - 1 
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1 
        arr[j + 1] = key
    return arr 

print(insertion_sort(arr))


# Time Complexity: Best O(n), Average O(n²), Worst O(n²).

# Space Complexity: O(1).
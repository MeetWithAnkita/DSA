arr = [2, 1, 0, 2, 1, 0, 1, 2, 0, 1]

# Your task:
# 1. Implement sort_colors(arr).
# 2. Use three pointers: low, mid, high.
# 3. Use while mid <= high.
# 4. Do not use sorted(), sort(), or a frequency dictionary.
# 5. Sort the original array in place.

def sort_colors(arr):
    low = 0 
    mid = 0 
    high = len(arr) - 1 

    while mid <= high:
        if arr[mid] == 0 :
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1 
            mid += 1 
        elif arr[mid] == 1 :
            mid += 1 
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1 
    return arr

print(sort_colors(arr))
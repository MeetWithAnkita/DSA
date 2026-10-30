arr = [8, 3, 5, 2, 9, 1, 6, 4, 6, 4]
def merge(left, right):
    result = []
    i = 0 
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1 
        else:
            result.append(right[j])
            j += 1 
    result.extend(left[i:])
    result.extend(right[j:])

    return result
        
def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    m = n // 2 

    left = merge_sort(arr[:m])
    right = merge_sort(arr[m:])

    return merge(left, right)

print(merge_sort(arr))


# In Merge Sort, we must preserve every element, including duplicates.
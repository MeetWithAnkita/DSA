# 1. What is Merge Sort?
# Merge Sort is a sorting algorithm that:
# 1. Divides an array into smaller halves.
# 2. Keeps dividing until every subarray contains just one element.
# 3. Merges those small arrays back together in sorted order.
# The main idea: Divide first, then sort while merging.

arr = [8, 3, 5, 2, 9, 1, 6, 4]

def merge(left, right):
    result = []
    i = 0 
    j = 0 
    
    # compare elements from both arrays
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
    # base condition
    if len(arr) <= 1:
        return arr

    # divide into two halves
    mid = (len(arr) // 2)
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid: ])

    # merge sorted halves
    return merge(left, right)

print(merge_sort(arr))


# Time and space complexity
# Case	Time complexity
# Best	O(n log n)
# Average	O(n log n)
# Worst	O(n log n)

# - Auxiliary space: O(n) for the temporary arrays used during merging.
# - Merge Sort is stable when equal elements from the left are selected first (<=).
# - It is not an in-place sorting algorithm in this implementation.


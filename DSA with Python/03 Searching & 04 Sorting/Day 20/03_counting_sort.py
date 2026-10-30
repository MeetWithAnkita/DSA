# What is Counting Sort?
# Counting Sort is a sorting algorithm that sorts 
# elements by counting how many times each value appears.

# Unlike Bubble Sort or Quick Sort, 
# it doesn't compare elements with each other.

arr = [4, 2, 2, 8, 3, 3, 1]


def counting_sort(arr):
    if not arr:
        return arr 
    max_value = max(arr) # 8 
    count = [0] * (max_value + 1 )
# count= | 0 || 0 || 0 || 0 || 0 || 0 || 0 || 0 || 0 ||
# index= | 0 || 1 || 2 || 3 || 4 || 5 || 6 || 7 || 8 ||
    for num in arr:
        count[num] += 1 
# count= | 0 || 1 || 2 || 2 || 1 || 0 || 0 || 0 || 1 ||
# index= | 0 || 1 || 2 || 3 || 4 || 5 || 6 || 7 || 8 ||

    index = 0 
    for num in range(len(count)):
        for j in range(count[num]):
            arr[index] = num
            index += 1 
    return arr

print(counting_sort(arr))


# Case	Complexity
# Best time	O(n + k)
# Average time	O(n + k)
# Worst time	O(n + k)
# Auxiliary space	O(k)

# Important: This implementation assumes non-negative 
# integers. If the maximum value is extremely large 
# compared with the number of elements, Counting Sort 
# may waste a lot of memory.
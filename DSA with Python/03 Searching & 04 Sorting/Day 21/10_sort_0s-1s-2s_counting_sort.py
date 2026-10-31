arr = [2, 0, 1, 2, 1, 0, 2, 1, 0]

def counting_sort(arr):
    max_value = max(arr)
    count = [0] * (max_value + 1 )

    for i in arr:
        count[i] += 1 

    arr1 = []
    for num in range(len(count)):
        for j in range(count[num]):
            arr1.append(num)
    return arr1

print(counting_sort(arr))


# Complexity	    Value
# Time	            O(n + k) = O(n), since k = 3
# Auxiliary space	O(k) = O(1), since k = 3
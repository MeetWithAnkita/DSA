arr = [3, 1, 3, 2, 1, 3]

def counting_sort(arr):
    if not arr:
        return arr 
    max_value = max(arr)
    count = [0] * (max_value + 1)

    for num in arr:
        count[num] += 1 

    index = 0 

    for num in range(len(count)):
        for j in range(count[num]):
            arr[index] = num
            index += 1 
    return arr

print(counting_sort(arr))
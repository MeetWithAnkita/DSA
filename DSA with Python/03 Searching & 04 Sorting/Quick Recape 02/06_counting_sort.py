arr = [6, 1, 4, 1, 3, 6, 2]

def counting_sort(arr):
    n = len(arr)
    if not arr:
        return arr
    
    max_value = max(arr)
    count = [0] * (max_value + 1)

    for i in arr:
        count[i] += 1 

    arr= []
    for num in range(len(count)):
        for j in range(count[num]):
            arr.append(num)
    return arr


print(counting_sort(arr))
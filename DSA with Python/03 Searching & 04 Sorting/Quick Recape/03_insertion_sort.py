arr = [9, 5, 7, 3, 8, 2]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i -1
        while 0<= j<i and arr[j] > key:
            # if arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1 
        arr[j + 1] = key
    return arr

print(insertion_sort(arr))

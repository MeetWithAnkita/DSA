arr = [3, 7, 3, 9, 3, 5]
target = 3

def find_all_occurrences(arr, target):
    index = []
    for i in range(len(arr)):
        if arr[i] == target:
            index.append(i)
    return index

print(find_all_occurrences(arr, target))
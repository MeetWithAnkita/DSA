arr = [5, 2, 5, 8, 5, 3, 2]
target = 5

def find_all_occurrences(arr, target):
    l = []
    for i in range(len(arr)):
        if target == arr[i]:
            l.append(i)
    return(l)
print(find_all_occurrences(arr, target))

# time: O(n)
# Space: O(k)

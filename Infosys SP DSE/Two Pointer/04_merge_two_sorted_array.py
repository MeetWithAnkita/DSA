arr1 = [1, 3, 5]
arr2 = [2, 4, 6]

def merge(arr1, arr2):
    i = 0 
    j = 0 
    l = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            l.append(arr1[i])
            i += 1
        else:
            l.append(arr2[j])
            j += 1

    l.extend(arr1[i:])
    l.extend(arr2[j:])
    return l

print(merge(arr1, arr2))
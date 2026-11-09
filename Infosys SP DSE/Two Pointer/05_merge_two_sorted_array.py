arr1 = [1, 4, 7, 9]
arr2 = [2, 3, 8]

def merge_two_array(arr1, arr2):
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

print( merge_two_array(arr1, arr2))
arr = [12, 5, 9, 2, 15, 7, 3, 10, 5]

def merge(left, right):
    result = [] 
    i = 0 
    j = 0 
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i +=1 
        else:
            result.append(right[j])
            j += 1 
    result.extend(left[i:])
    result.extend(right[j:])

    return result



def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    m = len(arr) // 2 

    left = merge_sort(arr[:m])
    right = merge_sort(arr[m:])

    return merge(left, right)

print(merge_sort(arr))

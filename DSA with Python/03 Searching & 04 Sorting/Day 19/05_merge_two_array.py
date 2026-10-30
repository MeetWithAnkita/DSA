left = [2, 5, 8]
right = [1, 4, 6]

def merge(left, right):
    result = []
    i = 0 
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1 
        else:
            result.append(right[j])
            j += 1 
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result 

print(merge(left, right))

# Complexity: 
# Time: \(O(n+m)\), Auxiliary space: \(O(n+m)\),
# where n and m are the lengths of the two input arrays.

matrix = [
    [1,  3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]

target = 16

def search_ele(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])
    s = 0 
    e = (rows * cols) - 1 
    while s <= e :
        mid = ( s + e ) // 2 
        r = mid // cols
        c = mid % cols 

        if matrix[r][c] == target:
            return True 
        elif matrix[r][c] < target:
            s = mid + 1 
        else:
            e = mid - 1 
    return False

print(search_ele(matrix, target))


# The important conversion
# \[
# row = mid // cols
# \]

# \[
# col = mid \% cols
# \]

# You don't need to flatten the matrix physically!

# Complexity	    Result
# Time	            O(log(rows × cols))
# Auxiliary Space   O(1)
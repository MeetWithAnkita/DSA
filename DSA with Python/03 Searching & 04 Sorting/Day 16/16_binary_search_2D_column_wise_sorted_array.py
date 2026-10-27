matrix = [
    [1,  4,  7, 11],
    [2,  5,  8, 12],
    [3,  6,  9, 16],
    [10, 13, 14, 17]
]


target = 5
def search(matrix, target):
    rows = len(matrix)      #4
    cols = len(matrix[0])   #4
    
    r = 0
    c = cols - 1

    while r < rows and c >= 0:
        current = matrix[r][c]
        if target == current:
            return (r, c )
        elif target < current:
            # current = matrix[r][c - 1] 
            c -= 1
        else:
            # current = matrix[r + 1][c]
            r += 1
    return "Not Found"
    
print(search(matrix, target))

# Time Complexity: \(O(rows + cols)\)
# Auxiliary Space: \(O(1)\)


# This searching technique is called Staircase Search 
# (also known as Search in a Row-wise and Column-wise 
# Sorted Matrix).
matrix = [
    [1,  3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]

# target = 30
target = 13

def search_ele(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])

    s = 0 
    e = (rows * cols) - 1
    while s <= e:
        m = ( s + e ) // 2 
        r = m // cols
        c = m % cols

        if target == matrix[r][c]:
            return True 
        elif target < matrix[r][c]:
            e  = m - 1 
        else:
            s = m + 1 
    return False


print(search_ele(matrix, target))
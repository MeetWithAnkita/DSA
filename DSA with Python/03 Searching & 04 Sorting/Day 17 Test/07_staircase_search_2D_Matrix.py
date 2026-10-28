matrix = [
    [1,  4,  7, 11],
    [2,  5,  8, 12],
    [3,  6,  9, 16],
    [10, 13, 14, 17]
]

target = 9

def staircase_problem(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])

    r = 0 
    c = cols - 1 

    while (0 <= r < rows) and (cols > c >= 0):
        current = matrix[r][c]
        if current == target:
            return (r, c)
        elif current > target:
            c -= 1 
        elif current < target:
            r += 1 
    return (-1, -1)

print(staircase_problem(matrix, target))
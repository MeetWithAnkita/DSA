board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

def check_valid_sudoku(board):
    # check rows
    def check_rows(row):
        seen = set()
        for i in range(len(board)):
            num = row[i]
            if num == ".":
                continue 
            elif num in seen:
                return False 
            else:
                seen.add(num)
        return True

    # check columns
    def check_cols(board, col):
        seen = set()
        for i in range(len(board)):
            num = board[i][col]
            if num == ".":
                continue 
            elif num in seen:
                return False 
            else:
                seen.add(num)
        return True
        

    # check all 3*3 boxs
    def check_boxs(board, start_row, start_col):
        seen = set()
        for i in range(start_row, start_row+3):
            for j in range(start_col, start_col+3):
                num = board[i][j]
                if num == ".":
                    continue 
                elif num in seen:
                    return False 
                else:
                    seen.add(num)
        return True
        

    # all valid rows
    for i in range(len(board)):
        if not check_rows(board[i]):
            return False 
    # all valid cols
    for i in range(len(board)):
        if not check_cols(board, i):
            return False
    # all valid 3*3 boxes
    for i in range(0, len(board), 3):
        for j in range(0, len(board), 3):
            if not check_boxs(board, i, j):
                return False
    return True

print(check_valid_sudoku(board))



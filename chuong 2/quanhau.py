def print_solution(board):
    for i in range(8):
        for j in range(8):
            print(board[i][j], end=" ")
        print()

def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, 8, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_util(board, col):
    if col == 8:
        return True
    for i in range(8):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_util(board, col + 1) == True:
                return True
            board[i][col] = 0
    return False

def solve():
    board = [[0 for x in range(8)] for y in range(8)]
    if solve_util(board, 0) == False:
        print("Khong co giai phap")
        return False
    print_solution(board)
    return True

solve()

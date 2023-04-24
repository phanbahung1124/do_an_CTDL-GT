def is_valid_move(x, y, board):
    n = len(board)
    return x >= 0 and x < n and y >= 0 and y < n and board[x][y] == -1


def knight_tour_helper(x, y, move_i, move_x, move_y, board):
    if move_i == len(board) ** 2:
        return True

    for i in range(len(move_x)):
        next_x = x + move_x[i]
        next_y = y + move_y[i]

        if is_valid_move(next_x, next_y, board):
            board[next_x][next_y] = move_i
            if knight_tour_helper(next_x, next_y, move_i + 1, move_x, move_y, board):
                return True
            board[next_x][next_y] = -1

    return False


def knight_tour(n):
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]
    board = [[-1 for j in range(n)] for i in range(n)]
    board[0][0] = 0

    if knight_tour_helper(0, 0, 1, move_x, move_y, board):
        print("Solution exists: ")
        for row in board:
            print(row)
        return board
    else:
        print("Solution does not exist.")
        return None
def main():
    n = abs(int(input('nhap kich thuoc cua ban co n*n : ')))
    knight_tour(n)

if __name__=='__main__':
    main()
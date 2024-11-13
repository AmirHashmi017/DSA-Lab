BOARD_SIZE = 4

def display_board(board):
    for row in board:
        print(" ".join(str(cell) for cell in row))
    print()

def is_position_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, BOARD_SIZE), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_n_queens_helper(board, col):
    if col >= BOARD_SIZE:
        return True
    for i in range(BOARD_SIZE):
        if is_position_safe(board, i, col):
            board[i][col] = 1
            if solve_n_queens_helper(board, col + 1):
                return True
            board[i][col] = 0
    return False

def solve_n_queens():
    board = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    if not solve_n_queens_helper(board, 0):
        print("No solution exists")
        return False
    display_board(board)
    return True

solve_n_queens()

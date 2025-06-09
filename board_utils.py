import copy

def print_board(board):
    for row in range(len(board)):
        print(board[row])

def copy_board(board):
    new_board = copy.deepcopy(board) 
    return new_board

def find_next_empty_cell(board):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 0:
                return (row,col)

def is_goal(board):
    size = len(board)
    box_size = int(size ** 0.5)
    
    for row in board:
        if 0 in row:
            return False

    for i in range(size):
        row = [n for n in board[i] if n != 0]
        col = [board[j][i] for j in range(size) if board[j][i] != 0]
        if len(row) != len(set(row)) or len(col) != len(set(col)):
            return False

    for box_row in range(0, size, box_size):
        for box_col in range(0, size, box_size):
            box = []
            for i in range(box_row, box_row + box_size):
                for j in range(box_col, box_col + box_size):
                    num = board[i][j]
                    if num != 0:
                        box.append(num)
            if len(box) != len(set(box)):
                return False

    return True 

    
def is_valid(board, cell, number):
    row, col = cell
    size = len(board)
    box_size = int(size ** 0.5)

    if number in board[row]:
        return False

    for r in range(size):
        if board[r][col] == number:
            return False

    box_row_start = (row // box_size) * box_size
    box_col_start = (col // box_size) * box_size

    for i in range(box_row_start, box_row_start + box_size):
        for j in range(box_col_start, box_col_start + box_size):
            if board[i][j] == number:
                return False

    return True

        
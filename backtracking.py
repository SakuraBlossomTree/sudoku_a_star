from board_utils import is_valid

def backtrack(board, row=0, col=0):

    if row == 8 and col == 9:
        return True
    
    if col == 9:
        row += 1
        col = 0
    
    if board[row][col] != 0:
        return backtrack(board, row, col + 1)
    
    for num in range(1, 10):
        if is_valid(board , (row, col), num):
            board[row][col] = num
            
            if backtrack(board, row, col + 1):
                return True 
            
            board[row][col] = 0

    return False

def solve(board):
    if backtrack(board):
        return board
    else:
        return None
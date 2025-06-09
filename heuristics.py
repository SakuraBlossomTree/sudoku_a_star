from board_utils import is_valid

def count_empty_cells(board):
    count = 0
    for row in board:
        count += row.count(0)
    return count

def advanced_heuristic(board):
    total_candidates = 0
    size = len(board)
    box_size = int(size ** 0.5)

    for i in range(size):
        for j in range(size):
            if board[i][j] == 0:
                candidates = 0
                for num in range(1, size + 1):
                    if is_valid(board, (i, j), num):
                        candidates += 1
                total_candidates += candidates

    return total_candidates
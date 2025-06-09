import random
import math

def generate_full_board(size):
    box_size = int(math.sqrt(size))
    numbers = list(range(1, size + 1))
    board = [[0] * size for _ in range(size)]

    def is_valid(r, c, num):
        for i in range(size):
            if board[r][i] == num or board[i][c] == num:
                return False
        box_r = (r // box_size) * box_size
        box_c = (c // box_size) * box_size
        for i in range(box_r, box_r + box_size):
            for j in range(box_c, box_c + box_size):
                if board[i][j] == num:
                    return False
        return True

    def fill():
        for r in range(size):
            for c in range(size):
                if board[r][c] == 0:
                    random.shuffle(numbers)
                    for num in numbers:
                        if is_valid(r, c, num):
                            board[r][c] = num
                            if fill():
                                return True
                            board[r][c] = 0
                    return False
        return True

    fill()
    return board

def make_puzzle(board, blanks):
    size = len(board)
    puzzle = [row[:] for row in board]
    positions = [(i, j) for i in range(size) for j in range(size)]
    random.shuffle(positions)
    for i in range(blanks):
        r, c = positions[i]
        puzzle[r][c] = 0
    return puzzle

# ===== Usage =====
size = 9 # Change to 9, 16, etc. (must be a perfect square)
blanks = 50  # Number of empty cells to make a puzzle

full_board = generate_full_board(size)
puzzle_board = make_puzzle(full_board, blanks)


